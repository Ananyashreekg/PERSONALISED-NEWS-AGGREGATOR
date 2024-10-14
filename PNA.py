import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch news based on the user's input
def get_news():
    api_key = "5c3780922ffe4beea37cb4a98a590574"  # Replace with your NewsAPI key
    keyword = keyword_entry.get()  # Get keyword entered by the user
    if keyword == "":
        messagebox.showerror("Input Error", "Please enter a keyword")
        return

    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == "ok":
            articles = data['articles']
            news_listbox.delete(0, tk.END)  # Clear previous results

            for article in articles[:10]:  # Show top 10 articles
                news_listbox.insert(tk.END, article['title'])

        else:
            messagebox.showerror("Error", "Unable to fetch news")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Personalized News Aggregator")

# Window size and layout
root.geometry("600x400")
root.config(bg="lightblue")

# Label for keyword input
keyword_label = tk.Label(root, text="Enter Keyword/Category:", bg="lightblue", font=("Arial", 12))
keyword_label.pack(pady=10)

# Entry field for keyword
keyword_entry = tk.Entry(root, width=40, font=("Arial", 14))
keyword_entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Search News", font=("Arial", 12), command=get_news)
search_button.pack(pady=10)

# Listbox to display the news headlines
news_listbox = tk.Listbox(root, height=10, width=80, font=("Arial", 12))
news_listbox.pack(pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
news_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=news_listbox.yview)

# Start the GUI loop
root.mainloop()
