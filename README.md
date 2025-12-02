# spam-classifier
Email Spam Classifier implemented from scratch using Python OOP
# Email Spam Classifier From Scratch

This project implements a **simple Email Spam Classifier** using **pure Python and Object-Oriented Programming (OOP)**.  
It **does not use any machine learning libraries** like scikit-learn or pandas — everything is built manually.

---

## 🔹 Project Overview

The classifier works by:

1. Reading a dataset of messages labeled as `spam` or `ham` (normal message).  
2. Counting word frequencies in spam and ham messages.  
3. Predicting new messages based on which set of words (spam or ham) is more frequent.

This is a **rule-based machine learning approach**, perfect for learning **basic ML logic**.

---

## 📁 Files in the Project

- `spam_model.py` — main Python code for training and predicting messages  
- `dataset.txt` — sample messages for training  
- `README.md` — project documentation  

---

## 🛠️ How to Run

1. Make sure you have **Python installed** (Python 3 recommended).  
2. Place all files in the same folder.  
3. Run the program in terminal:

```bash
python spam_model.py
