# Smishing Simulation Lab 🔐

An educational demonstration of smishing (SMS phishing) attacks built with Python Flask. This project simulates realistic phishing scenarios to help understand and defend against social engineering attacks.

## ⚠️ Disclaimer
**FOR EDUCATIONAL USE ONLY** - This tool is designed to demonstrate how phishing works so you can better recognize and prevent these attacks. Never use against real targets without explicit permission.

## 🎯 Features

- **3 Realistic Phishing Portals:**
  - Facebook Login Clone with urgency banners
  - SBI Bank two-step phishing (login + card details)
  - Apple ID Clone with device location spoofing

- **SMS Inbox Simulation:**
  - Mobile-style interface with 3 different phishing lures
  - Delivery, Bank, and Apple ID scam examples
  - Clickable shortened URLs (bit.ly)

- **Credential Harvesting:**
  - Automatic logging with timestamps
  - Terminal output for real-time monitoring
  - Card details capture for banking demo

- **Educational Components:**
  - Built-in red flag checklist
  - Clear warnings about educational purpose
  - Demonstrates psychological tricks (urgency, fear)

  **Mobile sms dashboard**
  

<img width="571" height="298" alt="image" src="https://github.com/user-attachments/assets/77dc8a6b-1d96-47b7-9881-998b46d6b407" />


 **facebook clone dashboard**
 
 <img width="559" height="296" alt="image" src="https://github.com/user-attachments/assets/20b588d2-23d3-4d63-a5d1-e541553dec18" />

 **sbi clone dashboard and alert**
 

 <img width="625" height="304" alt="image" src="https://github.com/user-attachments/assets/eebce422-e9f4-4b49-9b6a-801be0e76c92" />
 

<img width="626" height="322" alt="image" src="https://github.com/user-attachments/assets/ea9baa9b-cd22-417c-9d99-9fdb7eb52cba" />


<img width="626" height="314" alt="image" src="https://github.com/user-attachments/assets/576a19f1-9176-4d0f-81af-a1cc75b8a1d3" />


**apple_id clone dashboard and alert**


  <img width="625" height="314" alt="image" src="https://github.com/user-attachments/assets/9f01cab4-4b32-4451-8cf0-93c66d4dcef1" />
  

<img width="624" height="308" alt="image" src="https://github.com/user-attachments/assets/9720f293-6752-4b61-aa4c-13e4c477f6a8" />


**database overview**


<img width="688" height="539" alt="image" src="https://github.com/user-attachments/assets/cd9744b4-5d0a-437e-b09d-ffedd10ba78f" />



## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/smishing-lab-demo.git
cd smishing-lab-demo
```
2.**Create virtual environment**

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

3.**Install dependencies**

pip install -r requirements.txt

4.**Run the application**

python app.py

5.**Open your browser**

http://127.0.0.1:5000




