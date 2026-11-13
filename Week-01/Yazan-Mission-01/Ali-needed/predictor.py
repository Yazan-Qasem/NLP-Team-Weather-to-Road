import torch
import torch.nn.functional as F
import pandas as pd
from transformers import RobertaTokenizer, RobertaForSequenceClassification

# 1. إعداد الجهاز وتحميل النموذج المدرب (دقة 95%)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = "./final_roberta_nyc_model"  # مسار مجلد النموذج بعد فك الضغط

tokenizer = RobertaTokenizer.from_pretrained(MODEL_PATH)
model = RobertaForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(device)
model.eval()

# 2. قراءة ملف شوارع نيويورك المنظف
roads_df = pd.read_csv("NYC_Roads_Cleaned.csv")

def analyze_alert_and_predict_roads_smart(alert_text):
    inputs = tokenizer(alert_text, return_tensors="pt", truncation=True, padding=True, max_length=256).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred_class = torch.argmax(probs, dim=-1).item()
        confidence = probs[0][pred_class].item() * 100

    risk_map = {
        0: "Safe / No Closure",
        1: "Moderate Caution",
        2: "HIGH RISK - ROAD CLOSURE EXPECTED"
    }
    
    text_upper = alert_text.upper()
    hazard_type = "Flood" if "FLOOD" in text_upper else ("Snow/Ice" if any(w in text_upper for w in ["SNOW", "WINTER", "FREEZING", "ICE"]) else "Other")
    
    nyc_boroughs = ['MANHATTAN', 'NEW YORK', 'BRONX', 'BROOKLYN', 'KINGS', 'QUEENS', 'STATEN ISLAND', 'RICHMOND']
    affected_boroughs = [b for b in nyc_boroughs if b in text_upper]
    if not affected_boroughs:
        affected_boroughs = ['ALL NYC']

    result_summary = {
        "risk_level": pred_class,
        "risk_label": risk_map[pred_class],
        "confidence": round(confidence, 1),
        "hazard_type": hazard_type,
        "affected_boroughs": affected_boroughs
    }

    if pred_class >= 1:
        width_cols = [c for c in roads_df.columns if 'WIDTH' in c.upper()]
        if width_cols:
            at_risk_roads = roads_df[roads_df[width_cols[0]] <= 30].copy()
        else:
            at_risk_roads = roads_df.head(100).copy()
            
        at_risk_roads['Predicted_Status'] = 'CLOSED' if pred_class == 2 else 'CAUTION'
        at_risk_roads['Hazard_Reason'] = hazard_type
        return result_summary, at_risk_roads.head(50)
    else:
        return result_summary, pd.DataFrame()
