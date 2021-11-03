from modules import *

if not fileExists():
    txt = "ERROR - File 'data.xlsx' dose not exist."
    color = "red"
    text = colored(txt, color)
    print(text)
    print("Please add it and run program again to continue")
    raise SystemExit

try:
    objects = readData()
    if len(objects):
        driver, wait = initalizeDriver()
        # Visit Cargo Website
        driver.get("https://cargo.build/")
        waitForLogin()
        for o in objects:
            url = o.get('url', None)
            metadata = o.get('metadata', None)
            if url and metadata:
                scarpe(driver, wait, url, metadata)
        # driver.quit()
        print("Operation completed successfully!")
except Exception as e:
    print(e)
    print("There was a general error.")