# **Sentiment Analysis Web App**  
A **Streamlit-based** web application that performs **sentiment analysis** on user-provided text or news articles. It supports **multilingual text analysis** by using **Google Translate API** for automatic translation.

---

## 🚀 **Features**
✅ **Sentiment Analysis** using **VADER (NLTK's SentimentIntensityAnalyzer)**  
✅ **Supports Multiple Languages** via **Google Translate API**  
✅ **Two Modes**:  
   - **Text Analysis**: Users can enter any text for sentiment analysis.  
   - **News Article Analysis**: Users can provide a **URL**, and the app extracts and analyzes the sentiment of the summary.  
✅ **Graphical Visualization** of sentiment scores using **Matplotlib**  
✅ **User-friendly UI** built with **Streamlit**  

---

## 📌 **Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### **2️⃣ Create a Virtual Environment (Optional, but Recommended)**
```sh
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip3 install -r requirements.txt
```

---

## 📜 **Requirements**
The app requires the following **Python libraries**:
```sh
pip3 install streamlit
pip3 install nltk
pip3 install matplotlib
pip3 install newspaper3k
pip3 install deep-translator
```

---

## 🎯 **How to Run the App**
### **Run Locally**
```sh
streamlit run sentiment_app.py
```
The app will open in your **web browser**.

---

## 🛠️ **How It Works**
### **1️⃣ Sentiment Analysis on Text**
- The user enters a **text**.
- The app detects the **language**.
- If it's not **English**, it gets **translated**.
- The app performs **sentiment analysis** using **VADER (NLTK)**.
- It returns:
  - **Sentiment Score** (range: `-1` to `1`).
  - **Sentiment Category** (`Positive`, `Neutral`, `Negative`).
  - **Bar Chart** for visualization.

### **2️⃣ Sentiment Analysis on News Articles**
- The user enters a **news article URL**.
- The app **extracts the text** from the article.
- The text is analyzed for **sentiment**.
- A **graph** is generated.

---

## 📊 **Sentiment Score Interpretation**
| **Sentiment Score** | **Interpretation** |
|------------------|----------------|
| **`> 0`**  | Positive Sentiment |
| **`= 0`**  | Neutral Sentiment |
| **`< 0`**  | Negative Sentiment |


---

## 🏗️ **Future Improvements**
🔹 Add **Emotion Detection** (Happy, Sad, Angry, etc.)  
🔹 Use **Deep Learning models** for sentiment analysis  
🔹 Improve **language translation accuracy**  

---

## 📝 **License**
This project is **open-source**.

---

## 🤝 **Contributing**
Feel free to **fork** the repository, make improvements, and submit a **pull request**.


Happy Coding! 🚀
