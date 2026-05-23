# LMS Dashboard 📊

A full-stack LMS Dashboard project built using **FastAPI** and **React.js** to analyze and visualize students’ course-wise performance using interactive bar charts.

---

# 🚀 Features

* 📈 Course-wise student performance analysis
* 📊 Interactive Bar Chart visualization using Recharts
* ⚡ FastAPI backend with REST API
* ⚛️ React frontend with Axios data fetching
* 🔄 Real-time API integration
* 🧩 Component-based frontend architecture
* 🎨 Clean and simple UI

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Axios
* Recharts
* CSS

## Backend

* FastAPI
* Pydantic
* Uvicorn

---

# 📂 Project Structure

```text id="hthmvt"
lms-dashboard/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── mock_data.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── BarChartWidget.jsx
│   │
│   ├── package.json
│
└── README.md
```

---

# 📊 API Response Example

```json id="bgffem"
{
  "data": [
    {
      "course_name": "Math",
      "average_score": 78
    },
    {
      "course_name": "Science",
      "average_score": 85
    }
  ]
}
```

---

# 📸 Screenshot

## 🎨 Frontend

<img width="629" height="447" alt="Marks_barchart_dashboard" src="https://github.com/user-attachments/assets/bc3c5cbf-4022-4ec5-aef1-de8408e7578d" />


```

---

# 🧠 Learning Outcomes

* Building REST APIs using FastAPI
* Using Pydantic models for response validation
* Fetching API data using Axios
* Data visualization using Recharts
* React component-based architecture
* Frontend and backend integration
