with open('file1.txt', 'r') as file:
    # Read a line from the file
    line = file.readline()
    
    # Separate words by spaces and commas
    words = [word.strip() for word in line.replace(',', ' ').split()]
    
    print(words)