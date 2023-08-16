# Question 3: Hyperlink History

# A]
urls = {
    "https://codefirstgirls.com/": ["Courses", "Opportunities"],
    "https://codefirstgirls.com/courses/": ["CFGDegree", "Back"],
    "https://codefirstgirls.com/courses/cfgdegree/": ["Back"],
    "https://codefirstgirls.com/opportunities/": ["Ambassadors", "Back"],
    "https://codefirstgirls.com/opportunities/ambassadors/": ["Back"]
}

history = []

# B] The time and space complexity of creating a dictionary or a list with n elements is O(n) and O(n) space.

def print_page(url):
    print(f"You are currently on the URL {url}")
    print("Where are you clicking?")
    print(f"Options: {', '.join(urls[url])}")

# B] The first two print statements run in O(1) time (or "constant time") as they do not depend on input size.
# B] The third print statement runs in O(n) time (or "linear time"), as it depends on the number of options for the url.

current_url = "https://codefirstgirls.com/" # O(1) time, O(1) space
print_page(current_url)

while urls[current_url]: # O(log n) time, O(log n) space
    choice = input()
    if choice not in urls[current_url]:
        print("Invalid choice. Please try again.")
        continue
    if choice == "Back":
        current_url = history.pop()
    else:
        history.append(current_url)
        current_url = current_url + choice.lower() + "/"
    print_page(current_url)

# B] This while loop runs in O(log n) time, where n is the number of urls in the urls dictionary

# B] In big O notation, lower order terms and constant factors can be ignored so overall the solution runs in O(n) time.

# Assumptions:
# User input is valid and does not cause any errors or exceptions as code does not have any exception or error handling.
# The print and input functions are constant time and space operations.
# The number of options for each url is fixed which is assumed because the urls dictionary is predefined.
# Input size is measured by number of urls in dictionary, as the code depends on the dictionary for its functionality.