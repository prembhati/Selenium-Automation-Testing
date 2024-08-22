from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Path to ChromeDriver
service = Service('C:\\Windows\\chromedriver.exe')  # Replace with the actual path to your ChromeDriver

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open Instagram's login page
    driver.get("https://www.instagram.com/accounts/login/")

    # Step 2: Wait until the username field is present and enter credentials
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys('your_username')  # Replace with your Instagram username

    password_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys('your_Password')  # Replace with your Instagram password

    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Allow time for login process
    time.sleep(5)

     # Step 3: Handle the "Save your login  info?" popup
    time.sleep(3)  # Adding extra wait time to ensure the pop-up loads
    try:
        # Try locating "Not Now" button using XPath
        not_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
        )
        not_now_button.click()
        print("Clicked on 'Not Now' button.")
    except:
        print("Not Now button not found, trying alternative method.")
        try:
            # Try using JavaScript to click the "Not Now" button
            driver.execute_script("document.querySelector('button:contains(\"Not Now\")').click()")
            print("Clicked on 'Not Now' button using JavaScript.")
        except Exception as e:
            print(f"Failed to click on 'Not Now' button. Error: {e}")
   
    # Step 4: Navigate to your profile page
    try:
        profile_icon = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Profile']"))
        )
        profile_icon.click()
    except TimeoutException:
        print("Profile icon not found, taking a screenshot.")
        driver.save_screenshot('profile_icon_not_found.png')
        driver.quit()
        raise

    # Allow time for profile page to load
    time.sleep(5)

    # Step 5: Get the bio text and find all the links
    bio_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'biography')]"))
    )
    bio_text = bio_element.text

    # Assuming links are separated by spaces or newlines
    links = bio_text.split()

    # Step 6: Click each link in the bio
    for link in links:
        if link.startswith("http"):
            driver.get(link)
            time.sleep(5)  # Wait for the page to load
            driver.back()  # Go back to the profile page
            time.sleep(2)  # Wait for the profile page to reload

finally:
    driver.quit()
