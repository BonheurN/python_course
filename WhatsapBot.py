from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def whatsapp_bot():
    # Configuration - Edit these values
    PHONE_NUMBER = "+48501138971"  # Include country code
    MESSAGE = "This is an automated message sent by bot"

    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    try:
        # Wait for QR code scan (checking for chat list)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="pane-side"]'))
        )
        print("Successfully connected to WhatsApp Web")

        # Directly open chat with specific number
        driver.get(f"https://web.whatsapp.com/send?phone={PHONE_NUMBER}")

        # Wait for message input box to appear
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]'))
        )

        # Type and send message
        message_box.send_keys(MESSAGE)
        time.sleep(2)  # Allow message input to register

        # Click send button
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )
        send_button.click()

        print("Message sent successfully")
        time.sleep(5)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Failed to connect to WhatsApp Web")
    finally:
        driver.quit()


if __name__ == "__main__":
    whatsapp_bot()