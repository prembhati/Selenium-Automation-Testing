from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up ChromeDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open the browser maximized

# Path to ChromeDriver
service = Service('C:\\Windows\\chromedriver.exe')  # Replace with the actual path to your ChromeDriver

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram's login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the page to load
time.sleep(3)

# Enter your Instagram credentials
driver.find_element(By.NAME, "username").send_keys("anatoly_7837")  # Replace with your Instagram username
driver.find_element(By.NAME, "password").send_keys("Pbdsa@12")  # Replace with your Instagram password

# Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for login to complete
time.sleep(5)

# Navigate to your profile page
driver.get("https://www.instagram.com/anatoly_7837/")  # Replace 'your_username' with your Instagram username

# Wait for the profile page to load
time.sleep(3)

# Click on the "Edit Profile" button
driver.find_element(By.XPATH, "//button[contains(text(),'Edit Profile')]").click()

# Wait for the edit profile page to load
time.sleep(3)

# Clear the current bio and enter the new one
bio_textarea = driver.find_element(By.NAME, "biography")
bio_textarea.clear()  # Clear existing bio
bio_textarea.send_keys("This is my new bio with links! https://link1.com")  # Enter new bio text

# Submit the form to save the bio
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

# Wait for the changes to be saved
time.sleep(3)

# Close the browser
driver.quit()
