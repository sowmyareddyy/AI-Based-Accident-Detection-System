import cv2
from detection import AccidentDetectionModel
import numpy as np
import winsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import geocoder 

# ---------------- LOAD TRAINED MODEL ----------------
model = AccidentDetectionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX


# ---------------- LOCATION FUNCTION ----------------
def get_location():
    try:
        g = geocoder.ip('me')  # Fetches current location from your IP
        if g.ok and g.latlng:
            lat, lon = g.latlng
            return round(lat, 4), round(lon, 4)
        else:
            print("⚠️ Could not fetch location.")
            return None, None
    except Exception as e:
        print(f"⚠️ Error getting location: {e}")
        return None, None


# ---------------- EMAIL ALERT FUNCTION ----------------
def send_email_alert(probability):
    sender_email = "loll.llogic.69@gmail.com"
    receiver_email = "sowmyareddy1918@gmail.com"
    app_password = "agah izzy txjq ncty"  # <-- Gmail App Password

    lat, lon = get_location()
    if lat and lon:
        location_url = f"https://www.google.com/maps?q={lat},{lon}"
        location_text = f"{lat}, {lon}"
    else:
        location_url = "Location not available"
        location_text = "Unavailable"

    subject = "🚨 Accident Detected Alert"
    body = (
        f"🚧 Accident Detected!\n\n"
        f"📊 Confidence: {probability}%\n"
        f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"📍 Location: {location_text}\n\n"
        f"View on Map: {location_url}\n\n"
        f"Please check the live feed immediately!"
    )

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print(f"📧 Email alert sent successfully! ({location_text})")
    except Exception as e:
        print(f"⚠️ Error sending email: {e}")


# ---------------- MAIN APPLICATION ----------------
def startapplication(use_camera=False):
    if use_camera:
        video = cv2.VideoCapture(0)
        print("🎥 Using live webcam feed...")
    else:
        video = cv2.VideoCapture("Demo.gif")
        print("🎬 Using demo video (Demo.gif)...")

    if not video.isOpened():
        print("❌ Error: Could not open video source.")
        return

    alert_sent = False
    last_email_time = 0

    while True:
        ret, frame = video.read()
        if not ret or frame is None:
            print("⚠️ Warning: Empty frame received, skipping...")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])

        if pred == "Accident":
            prob = round(prob[0][0] * 100, 2)
            cv2.rectangle(frame, (0, 0), (480, 60), (0, 0, 0), -1)
            cv2.putText(frame, f"{pred} ({prob}%)", (20, 40), font, 1, (0, 255, 255), 2)

            if prob > 90:
                winsound.Beep(1000, 500)
                current_time = time.time()

                if not alert_sent or (current_time - last_email_time) > 30:
                    send_email_alert(prob)
                    alert_sent = True
                    last_email_time = current_time
        else:
            alert_sent = False

        cv2.imshow("🚨 Accident Detection System", frame)

        if cv2.waitKey(33) & 0xFF == ord("q"):
            print("👋 Exiting...")
            break

    video.release()
    cv2.destroyAllWindows()


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    # Change to True if you want to use your webcam
    startapplication(use_camera=False)
