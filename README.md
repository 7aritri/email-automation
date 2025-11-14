
# Email Automation 🚀

An email automation tool built with Python that helps you send, schedule, and manage emails more efficiently.

## 🔍 Features
- Send emails via SMTP or an email service provider  
- Schedule emails to be sent at specified times  
- Load recipient lists (CSV/JSON) and personalize messages  
- Optionally use templates (subject/body) with placeholders  
- Logging of send status and simple error handling  

## 🗂 Project Structure
```

email-automation/
│── main.py             # Entry point of the application
│── config.py           # Configuration (SMTP settings, credentials)
│── templates/          # Email body templates
│── recipients.csv      # Sample list of recipients
│── README.md
│── requirements.txt

```

## 🧰 Requirements
- Python 3.8 or above  
- A working SMTP server or service (Gmail, SendGrid, etc.)  
- `pip install -r requirements.txt`  

## ▶️ How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/7aritri/email-automation.git
````

2. Navigate into the project directory:

   ```bash
   cd email-automation
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure your SMTP details in `config.py` (or via environment variables).
5. Run the tool:

   ```bash
   python main.py
   ```

## 🎛 Configuration

Edit `config.py` (or environment variables) with these details:

* `SMTP_HOST` – your SMTP server address
* `SMTP_PORT` – port (usually 587 for TLS)
* `SMTP_USER` – your email address or user credential
* `SMTP_PASS` – your password or app-specific password
* `SENDER_NAME` – display name for the email
* `TEMPLATE_PATH` – path to your email template file
* `RECIPIENT_LIST` – path to your recipients file (CSV/JSON)

## 📨 Usage Example

* Create a template file, e.g., `templates/welcome.txt`:

  ```
  Subject: Welcome, {{first_name}}!

  Hello {{first_name}},

  Thanks for joining us. We’re excited to have you!

  Best regards,
  {{sender_name}}
  ```

* Create `recipients.csv`:

  ```
  email,first_name
  alice@example.com,Alice
  bob@example.com,Bob
  ```

* Run `python main.py` and watch the tool send personalized emails.

## 🧠 What This Project Demonstrates

* Working with SMTP and email protocols in Python
* Template rendering and personalization logic
* Scheduling tasks and managing asynchronous sends
* Logging and simple error-handling flows
* Clean modular code design (configuration, templates, sending logic)

## 🛠 Possible Improvements

* Add support for HTML emails and attachments
* Use OAuth2 or service-specific API keys (e.g., Gmail API) for authentication
* Add retry logic and exponential back-off for failed sends
* Build a CLI interface or a web dashboard for scheduling
* Integrate a database to track history and send statuses
* Add unit tests and CI/CD pipeline for robustness
* Package as a pip module for re-use

## 📚 Learning Benefits

This project is a strong portfolio piece for:

* Backend automation scripts
* Python libraries/tools (real-world I/O, network calls)
* Interview discussions around email protocols, scheduling logic, and design decisions
* Showcasing initiative: “I built an end-to-end tool for a common business need”


