# 🚦 Early Warning System for Winter Road Closure Prediction in NYC using NLP
## 🛠️ نظام الإنذار المبكر للتنبؤ بإغلاق طرق نيويورك في الشتاء باستخدام معالجة اللغات الطبيعية

---

## 📌 Project Overview | نبذة عن المشروع
**English:**  
This project is an AI-powered Predictive Early Warning System designed to anticipate winter road closures, flash floods, and heavy snow accumulations across New York City (NYC) boroughs **24 to 48 hours before the blizzard or storm hits**. The system leverages Natural Language Processing (NLP) to read and analyze official upcoming weather forecasts and warnings, mapping them against historical geographical thresholds of NYC streets to provide a live, color-coded predictive dashboard for citizens and city authorities.

**بالعربية:**  
هذا المشروع عبارة عن **نظام إنذار مبكر تنبؤي واستباقي** يهدف إلى معرفة الشوارع والمناطق المعرضة للإغلاق في مدينة نيويورك (بسبب السيول، الفيضانات المفاجئة، وتراكم الثلوج) **قبل حدوث العاصفة بـ 24 إلى 48 ساعة**. يعتمد النظام على قراءة وتحليل نصوص النشرات والتحذيرات الجوية المستقبلية باستخدام معالجة اللغات الطبيعية (NLP)، ثم مطابقتها مع الطبيعة الجغرافية والتاريخية لشوارع نيويورك لتوليد خارطة إنذار مبكر تفاعلية ملونة تخدم المواطنين والجهات المعنية.

---

## 🗺️ Project Roadmap & Structure | مخطط وهيكل المشروع

> [!NOTE]
> **Current Project Status (As of Nov 10, 2026):** We are currently in **End of Week 1** of development, executing independent parallel tasks as scheduled.
> **حالة المشروع الحالية (تحديث 10 تشرين الثاني 2026):** نحن الآن في **نهاية الأسبوع الأول** من التطوير، حيث يقوم كل عضو بتنفيذ مهامه المستقلة بالتوازي وفق الجدول الزمني.

### 🖼️ Project Structure Diagram | مخطط هيكل المشروع
![Project Roadmap](Project-Structure/project_roadmap.jpg)


---

## 📂 Repository Architecture | تقسيم وهيكلية المستودع
**English:**  
To ensure zero-dependency parallel development, the repository is structured into weekly phases. Each team member has a dedicated sub-folder within the weeks to push their standalone code, eliminating merge conflicts.

**بالعربية:**  
لضمان عمل الفريق بشكل متوازٍ ومستقل تماماً بدون اعتمادات متبادلة، تم تقسيم المستودع إلى أسابيع زمنية. ويحتوي كل أسبوع على مجلد خاص باسم العضو ومهمته الفرعية لتفادي أي تداخل برمي أثناء الرفع.

```text
📁 Your-Project-Repository/
│
├── 📁 Project_Structure/                # Project structure, diagrams, and documentation
│   └── 🖼️ project_roadmap.png          # Roadmap visual architecture
│
├── 📁 Week_01/                          # Week 1: Independent Baseline Foundation (Completed)
│   ├── 📁 01_Member1_Data_Scraper/      # NYC Open Data & NWS API collector script
│   ├── 📁 02_Member2_Preprocessing/     # English text cleaning and tokenization logic
│   ├── 📁 03_Member3_NLP_Model/         # Baseline RoBERTa/BERT classification setup on Kaggle
│   ├── 📁 04_Member4_UI_Dashboard/       # Streamlit mock UI layout & geographic map skeleton
│   └── 📁 05_Member5_Backend_Database/  # Google Sheets setup & mock API JSON endpoint building
│
├── 📁 Week_02/                          # Week 2: Feature Deepening & Predictive Logic (In Progress 🛠️)
│   ├── 📁 01_Member1_Geo_Data/          # Neighborhood mapping (Manhattan, Brooklyn, etc.)
│   ├── 📁 02_Member2_Labelling/         # Custom dataset annotations & text tagging
│   ├── 📁 03_Member3_Predictive_Logic/  # Developing the threshold matching predictive logic
│   ├── 📁 04_Member4_Advanced_UI/       # Multi-filters & 24h/48h predictive timeline visualization
│   └── 📁 05_Member5_API_Testing/       # Backend integration & Postman API testing endpoints
│
├── 📁 Week_03/                          # Week 3: Final Integration & Deployment (Upcoming)
│   └── 📁 Final_Integration_Code/       # Merged code combining UI, Backend API, and trained NLP Model
│
└── 📁 Testing_and_Reviews/              # Evaluation reports, accuracy matrices, and presentation slides
```

---

## 🛠️ Tech Stack & Ecosystem | الأدوات والمواقع المستخدمة

*   **Collaboration & Management:** [GitHub](https://github.com), [Trello](https://trello.com) / Notion
*   **Data & NLP Core (Python):** [Kaggle](https://kaggle.com) (Free GPU NVIDIA T4), [Hugging Face](https://huggingface.co) (RoBERTa / BERT-base)
*   **NYC Geo-Datasets:** [NYC Open Data Portal](https://cityofnewyork.us), [National Weather Service (NWS) API](https://weather.gov), OpenStreetMap ([Geofabrik](https://geofabrik.de))
*   **Backend & Database:** [VS Code](https://visualstudio.com), [Postman](https://postman.com), [Google Sheets](https://google.com) / SQLite
*   **UI & Live Maps:** [Streamlit](https://streamlit.io), Folium / Mapbox Python Library

---

## 👥 Core Team Roles | توزيع أدوار الفريق
1.  **Student 1 (Data & Geo-Engineer):** Responsible for data collection from NYC Open Data/NWS and spatial geographic mapping.
2.  **Student 2 (Data Preprocessing Specialist):** Responsible for text cleaning, data pipelines, and dataset labelling.
3.  **Student 3 (NLP & AI Machine Learning Engineer):** Responsible for training the language model and building the threshold-based predictive logic.
4.  **Student 4 (UI/UX Front-End Developer):** Responsible for constructing the interactive dashboard and map visualization via Streamlit.
5.  **Student 5 (Backend & API Architecture Engineer):** Responsible for database management, endpoint development, and full-stack integration.
