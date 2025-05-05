import json
import requests
import random

# Task 1: JSON Parsing
def parse_students_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for student in data['students']:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("File not found!")
    except json.JSONDecodeError:
        print("Error reading JSON data.")

# Task 2: Weather API (Fetch Weather Data)
def get_weather_data(city_name):
    api_key = "YOUR_API_KEY"  # You'll need to get your API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("Failed to retrieve data.")

# Task 3: JSON Modification (Books JSON)
def modify_books_json(file_path):
    try:
        with open(file_path, 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []

    print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book publication year: ")
        books.append({"title": title, "author": author, "year": year})
        print(f"Book '{title}' added.")

    elif choice == '2':
        title_to_update = input("Enter the title of the book to update: ")
        for book in books:
            if book['title'] == title_to_update:
                new_title = input(f"Enter new title (current: {book['title']}): ")
                new_author = input(f"Enter new author (current: {book['author']}): ")
                new_year = input(f"Enter new year (current: {book['year']}): ")
                book['title'] = new_title
                book['author'] = new_author
                book['year'] = new_year
                print(f"Book '{title_to_update}' updated.")
                break
        else:
            print("Book not found.")

    elif choice == '3':
        title_to_delete = input("Enter the title of the book to delete: ")
        books = [book for book in books if book['title'] != title_to_delete]
        print(f"Book '{title_to_delete}' deleted.")

    elif choice == '4':
        with open(file_path, 'w') as file:
            json.dump(books, file, indent=4)
        print("Changes saved.")

    else:
        print("Invalid option.")

# Task 4: Movie Recommendation System (OMDB API)
def movie_recommendation(genre):
    api_key = "YOUR_API_KEY"  # You'll need to get your API key from OMDB API
    url = f"http://www.omdbapi.com/?s={genre}&apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            movies = data['Search']
            random_movie = random.choice(movies)
            print(f"Recommended {genre} movie:")
            print(f"Title: {random_movie['Title']}")
            print(f"Year: {random_movie['Year']}")
            print(f"IMDB ID: {random_movie['imdbID']}")
        else:
            print(f"No movies found for genre '{genre}'.")
    else:
        print("Failed to retrieve data.")

# Main Menu
def main():
    while True:
        print("\nSelect a task:")
        print("1. JSON Parsing (Student details)")
        print("2. Weather API")
        print("3. Modify Books JSON")
        print("4. Movie Recommendation System")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_path = input("Enter the path to the students.json file: ")
            parse_students_json(file_path)
        
        elif choice == '2':
            city_name = input("Enter city name (e.g., Tashkent): ")
            get_weather_data(city_name)
        
        elif choice == '3':
            file_path = input("Enter the path to the books.json file: ")
            modify_books_json(file_path)
        
        elif choice == '4':
            genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ")
            movie_recommendation(genre)
        
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


