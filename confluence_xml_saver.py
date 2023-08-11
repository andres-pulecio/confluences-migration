# This script logs in to a Confluence website using provided credentials, navigates to a list of spaces and useres, and export all the information in .zip file.

# Note: Please replace the "<PASSWORD>" placeholder in the "headers" dictionary with a valid access for Confluence.

# Author: Andres Pulecio (apulecio)

# Import necessary modules
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import os.path

# Confluences Credentials
username = "apulecio"
password = "<PASSWORD>"

def verificar_archivos_con_extension_en_ruta(ruta, extension):
    if os.path.exists(ruta):
        archivos_en_ruta = [archivo for archivo in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, archivo))]
        archivos_con_extension = [archivo for archivo in archivos_en_ruta if archivo.endswith(extension)]
        return len(archivos_con_extension) > 0
    else:
        return False

# Function to save a web page using the context menu in Chrome
def save_page_with_context_menu(url):
    
    # Initialize Chrome driver
    driver = webdriver.Chrome()
    
    # Open the provided URL
    driver.get(url)
    
    # Enter username and password and click login button
    driver.find_element("id", "os_username").send_keys(username)
    driver.find_element("id", "os_password").send_keys(password)
    driver.find_element("id", "loginButton").click()
    
    # Wait for the page to load completely
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    
    # Check for login errors
    error_message = "Incorrect username or password."
    errors = driver.find_elements("css selector", ".flash-error")
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")
    
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    
    #Find check xml export
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="space-tools-body"]/div/form/fieldset/div[2]/label/div'))).click()
   
    #Find Buttom Next >> buttom
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="space-tools-body"]/div/form/div/div/input'))).click()
    print("[+] Find Buttom Next >> buttom")
    # Wait for a few seconds before saving the page
       
    #Login again!!!
    # Enter username and password and click login button
    try: 
        driver.find_element("id", "os_username").send_keys(username)
        driver.find_element("id", "os_password").send_keys(password)
        driver.find_element("id", "loginButton").click()
        print("[+] Login Need")
    except:
        print("[!] No Login Need")
    
    #Find Export buttom
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="space-tools-body"]/div/form/div[2]/div/input'))).click()
       
    #Find Dowload here Link
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="taskCurrentStatus"]/a'))).click()
    #Wait until file is dowload
    while verificar_archivos_con_extension_en_ruta('/Users/apulecio/Downloads', '.xml.zip')==False:
        time.sleep(1)
    #Close driver
   
    driver.quit()

# Function to execute a Linux shell command and capture the output
def ejecutar_comando_linux(comando):
    try:
        salida = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        return True, salida.strip()
    except subprocess.CalledProcessError as e:
        return False, e.output.strip()

# Main function
def main():
    # List of URLs to save
    urls_to_save = [
        '~jzhang1', '~ekim', '~jnavarro', '~jtaylor', '~dtumbusch', '~mbrumley', '~rscherercc', '~pwu', '~jwhitecc', '~gjangili@csc.com', '~dmwright', '~swathi.somareddy@applabs.com', '~sdasu', '~jsparks', '~lzhang', '~tsnider', '~eyan', '~jkrommcc', '~dkrommcc', '~dmillen', '~jfontaine', '~zzhang', '~jsnook', '~csealey', '~mallikarjuna.vennapusa@applabs.com', '~mhajekcc',
    ]

    # Loop through the URLs and save each page
    for url in urls_to_save:
        try:
            save_page_with_context_menu("https://confluence.bbpd.io/spaces/exportspacewelcome.action?key=" + url)
            page_id = url.split('=')[-1]
            nombre_archivo = f"{page_id}"
            ejecutar_comando_linux(f'mv ~/Downloads/* ./files-to-upload/{nombre_archivo}.xml.zip')
            ejecutar_comando_linux('find ~/Downloads -name ".*" -type f -exec rm {} \;')
            ejecutar_comando_linux('find ~/Downloads -name ".*" -type f -exec rm {} \;')
            print(f"[+] COMPLETED: {nombre_archivo}")
            ejecutar_comando_linux(f'echo [+] SUCCESS: {nombre_archivo} >> history.log')
        except:
            page_id = url.split('=')[-1]
            nombre_archivo = f"{page_id}"
            ejecutar_comando_linux(f'echo [!] ERROR: {nombre_archivo} >> history.log')
            ejecutar_comando_linux('find ~/Downloads -name ".*" -type f -exec rm {} \;')
    print("Process completed...")

if __name__ == "__main__":
    main()