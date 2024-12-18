from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get("https://app.quso.ai/auth/login-with-email")
driver.maximize_window()
time.sleep(5)

# Login Steps
enter_email = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div/div[4]/div[2]/form/div[1]/div[1]/div[2]/input')
enter_email.send_keys("vikram0812+intern@proton.me")
time.sleep(3)

enter_password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/section/div/div[4]/div[2]/form/div[1]/div[2]/div[2]/input")
enter_password.send_keys("Intern@2024")
time.sleep(3)

driver.find_element(By.ID, "login-with-email-btn").click()
time.sleep(6)  # Wait for login

# click ai generator video
ai_video = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/p[1]')
ai_video.click()

time.sleep(5)

# type script
type_script = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/textarea')
type_script.click()
type_script.send_keys('Test')
time.sleep(5)

# click continue
continue_click = driver.find_element_by_xpath('//*[@id="describe-script-continue-button"]')
continue_click.click()
time.sleep(5)

# Generate script
script = driver.find_element_by_xpath('//*[@id="text-to-video-generate-video-button"]')
script.click()
time.sleep(6)

# Generate Video
video_genearate = driver.find_element_by_xpath('//*[@id="text-to-video-generate-video-button"]')
video_genearate.click()
time.sleep(15)


# click all download video
all_download = driver.find_element_by_xpath('//*[@id="home-sidebar-nav-btn-All downloads"]')
all_download.click()
time.sleep(5)

download_video = driver.find_element_by_xpath('//*[@id="download-render-video-review-clip-download-page"]')
download_video.click()

time.sleep(30)


driver.quit()
