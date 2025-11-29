import pandas as pd
import matplotlib.pyplot as plt

data = {
     "Task": [
        "Requirement Gathering & Planning",
        "System Design (SRS, DFD, Use Case)",
        "Frontend Development (HTML, CSS, JS)",
        "Backend Development (Django Models, Views, URLs)",
        "Database Design & Integration",
        "Testing (Black Box, Unit Tests)",
        "AI Chatbot Integration (Gemini API)",
        "Deployment & AWS Setup",
        "Final Report & Presentation"
    ],
    "Start": [
        "2025-10-01", "2025-10-02", "2025-10-04", "2025-10-04", "2025-10-10",
        "2025-10-20", "2025-11-01", "2025-11-05", "2025-12-01"
    ],
    "End": [
        "2025-10-02", "2025-10-04", "2025-10-10", "2025-10-20", "2025-10-16",
        "2025-10-30", "2025-11-05", "2025-11-10", "2025-12-02"
    ]
}

df=pd.DataFrame(data)
df["Start"]=pd.to_datetime(df["Start"])
df["End"]=pd.to_datetime(df["End"])
df["Duration"]=(df["End"]-df["Start"]).dt.days

plt.figure(figsize=(12,6))
for i in range(len(df)-1, -1, -1):
    plt.barh(df["Task"][i], df["Duration"][i], left=df["Start"][i], color="skyblue", edgecolor="black")

plt.title("Gantt Chart: Society Connect Project Timeline", fontsize=14, fontweight="bold")
plt.xlabel("Timeline (2025)", fontsize=12)
plt.ylabel("Project Phases", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()