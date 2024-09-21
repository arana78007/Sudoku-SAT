from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome() 
 

def scrape_sudoku_entries(url):
    driver = webdriver.Chrome() 
    
    grid = []
    
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(3)

    # Switch to the frame that contains puzzle
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "frame"))

    
    for row in range(9):
        rowvalues = []
        for col in range(9):  
            input_id = f'f{col}{row}'  
            try:
                input_element = driver.find_element(By.ID, input_id)
                input_value = input_element.get_attribute('value').strip()  #
                if input_value:
                    try:
                        # Try to convert to integer
                        rowvalues.append(int(input_value))
                    except ValueError:
                        # If conversion fails, keep it as a string
                        rowvalues.append(input_value)
                else:
                    rowvalues.append('')  # Keep empty cells as empty strings
            except Exception as e:
                print(f"Error finding element with ID {input_id}: {e}")
                rowvalues.append(0)
        
        grid.append(rowvalues)
                
    driver.quit()
    return grid

    
                
# Example
#url = 'http://www.websudoku.com/'  
#scrape_sudoku_entries(url)

# Close the browser when done
#driver.quit()



