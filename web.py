import webbrowser as wb

query = input("Enter the query : ")

wb.open_new_tab(f'http://google.com/?q={query}') 
