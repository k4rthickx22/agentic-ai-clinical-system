🧠 Agentic AI Clinical Diagnosis System
An intelligent multi-agent medical assistant that analyzes patient symptoms, evaluates risk severity, suggests possible diagnoses, and generates structured medical reports.
Built using an Agentic AI architecture where multiple specialized agents collaborate to simulate clinical reasoning.
🚀 Project Overview
This system mimics real-world medical triage using AI agents:
Collects patient symptoms
Performs weighted symptom analysis
Evaluates severity & risk level
Suggests differential diagnoses
Recommends treatment plans
Generates a professional medical PDF report
The system is designed for structured reasoning rather than simple keyword matching.

🏗️ Architecture (Agent-Based Design)
The system consists of multiple intelligent agents:
👤 PatientAgent
Processes and structures user input
Extracts symptom information

💊 DrugAgent
Suggests medications based on diagnosis
Provides precautionary advice

⚠️ RiskAgent
Evaluates patient risk level
Identifies red-flag symptoms

🧠 SeverityAgent
Determines severity (Mild / Moderate / Severe)
Applies symptom weighting logic

🧾 DecisionAgent
Performs final diagnosis reasoning
Generates structured output

🛠️ Tech Stack
Python
Streamlit (Frontend UI)
Multi-Agent Architecture
Rule-based + Weighted Diagnosis Logic
PDF Report Generation
Virtual Environment (venv)

📂 Project Structure
drug_agent_project/
│
├── agents/
│   ├── patient_agent.py
│   ├── drug_agent.py
│   ├── risk_agent.py
│   ├── severity_agent.py
│   └── decision_agent.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/k4rthickx22/agentic-ai-clinical-system.git
cd agentic-ai-clinical-system
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
streamlit run app.py

📊 Features
✔ Multi-Agent Decision Architecture
✔ Symptom-Based Weighted Diagnosis
✔ Risk & Severity Evaluation
✔ Treatment Plan Recommendation
✔ Professional PDF Medical Report
✔ Modular and Scalable Design

🎯 Future Improvements
LLM integration for advanced reasoning
Semantic symptom similarity detection
Clinical dataset training
Real-time API-based medical validation
User authentication & patient history tracking
Deployment (Render / AWS / Azure)

⚠️ Disclaimer
This system is for educational and research purposes only.
It does not replace professional medical consultation.

👨‍💻 Author
Karthick Kalaivanan
GitHub: https://github.com/k4rthickx22

🔥 After Adding This

Run:
git add README.md
git commit -m "Added professional README"
git push
