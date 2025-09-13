
# Study Buddy

### An AI-powered cognitive tutor for mastering any subject.

[**Live Demo**](https://study-buddy-ai-tutor.onrender.com)

AIML Navigator is a full-stack web application that acts as a personal AI mentor to help users learn any complex subject. From technical fields like "Deep Learning" to creative skills like "Music Theory," the application provides a structured, interactive, and deeply contextual learning experience, guiding any user from novice to knowledgeable.

## The Problem

Learning a new, complex subject is incredibly challenging for self-learners. They often face information overload, a lack of structured paths, generic content that fails to connect concepts, and ineffective quizzes that test memorization over true understanding. AIML Navigator was built to solve these problems.

## Core Features

* **🧠 Personalized Roadmap Generation:** Enter any topic, and the AI generates a logical, step-by-step learning curriculum, breaking the subject down into manageable modules.

* **📖 Context-Aware Explanations:** Get in-depth explanations for each step. The AI explains *why* each concept is crucial for the main topic, using analogies and connecting theory to practice.

* **🎯 Content-Grounded Smart Quizzes:** Test your knowledge with application-based questions generated *exclusively* from the explanation text you just read, ensuring 100% relevance.

* **💬 Interactive AI Tutor:** Have a follow-up question? Chat with the AI Tutor, which has the full context of the main topic and the specific sub-topic you're studying.

* **⚖️ Compare & Contrast Tool:** Enter any two concepts to get a dynamic, AI-generated comparison table, perfect for clarifying confusing ideas.

## Technology Stack

This project is a full-stack application built with a modern and robust technology stack:

* **Backend:** **Python** with the **Flask** web framework.

* **AI Integration:** **Google Gemini 1.5 Flash** via the `google-generativeai` library.

* **Frontend:** **HTML**, **Tailwind CSS**, and modern **JavaScript**.

* **Deployment:** Hosted globally on **Render** with a **Gunicorn** production server.

## Local Setup and Installation

To run this project on your local machine, please follow these steps:

**1. Prerequisites:**

* Python 3.7+

* Git

* A Google Gemini API Key

**2. Clone the Repository:**

```

git clone [https://github.com/](https://github.com/)\<sahilawatramani>/\<Study-Buddy---AI-Tutor>.git
cd \<Study-Buddy---AI-Tutor>

```

**3. Create and Activate a Virtual Environment:**

```

# For macOS/Linux

python3 -m venv venv
source venv/bin/activate

# For Windows

python -m venv venv
.\\venv\\Scripts\\activate

```

**4. Install Dependencies:**

```

pip install -r requirements.txt

```

**5. Set Up Your API Key:**

* Create a file named `.env` in the root of the project directory.

* Add your Gemini API key to this file:

```

GEMINI_API_KEY="YOUR_API_KEY_HERE"

```

**6. Run the Application:**

```

flask run

```

The application will be available at `http://12.0.0.1:5000`.

## Scaling and Future Work

The application is architected for scalability using a stateless backend. Future development will focus on:

* **Database Integration:** Integrating a database like PostgreSQL or Firestore to manage user accounts and save learning progress.

* **Caching:** Implementing caching strategies for popular topics to reduce API calls and improve performance.
```
