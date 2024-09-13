## Introduction

<p align="justify">A notification system is a combination of software and hardware that provides a means of delivering a message to a set of intended recipients. These days having a notification system for your work setting is essential because technological advancements have improved considerably.
<p align="justify">And with these advancements, managing the work-life balance has become difficult. Moreover, staying updated with the latest trend and new notifications are very important. Almost all modern web applications these days possess notification facilities in their services. These systems have become an essential and integral aspect of modern Web applications.

## Usage Instructions

1. Clone this repository using the command:
   ```bash
   git clone https://github.com/devsofmukesh/automations.git
   ```

2. Navigate to the **Voice Notifications Automated** directory:
   ```bash
   cd Voice-Notifications-Automated
   ```

3. Open the `voice-notifier.py` file and update it with:
   - Your **Twilio** `account_sid` and `auth_token`
   - Your custom voice message in the `voice_message` variable
   - The **Twilio-issued** phone number and the target user's phone number

4. Save the changes.

5. Open a terminal (PowerShell/CMD/Bash) in the project directory and run:
   ```bash
   python voice-notifier.py
   ```

6. Wait for a minute, and the target user will receive a call from your Twilio-issued phone number with the voice message.

## Advanced Possibilities

<p align="justify">This prototype offers a wide range of potential applications. For example, you could implement it as a notification system for your team within an organization. It can also be used to deliver sales pitches to your target audience, provided you avoid spamming. Additionally, you could even use it for fun, such as playing pranks on your friends. The possibilities are endless!

