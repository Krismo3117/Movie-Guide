def display_menu():
    print("===== Movie List Management =====")
    print("1. Display all movie titles")
    print("2. Add a movie title")
    print("3. Delete a movie title")
    print("4. Exit")
    print("=============================")

def prepopulate_movie_list():
    return ["The Hangover", "E.T.", "John Wick 1"]

def display_all_titles(movie_list):
    print("===== Movie List =====")
    for title in movie_list:
        print(title)
    print("======================")

def add_title(movie_list, new_title):
    movie_list.append(new_title)
    print(f"'{new_title}' has been added to the list.")
    display_all_titles(movie_list)

def delete_title(movie_list, index):
    if index < 0 or index >= len(movie_list):
        print("Invalid index. Movie not deleted.")
    else:
        deleted_title = movie_list.pop(index)
        print(f"'{deleted_title}' has been deleted from the list.")
        display_all_titles(movie_list)

def main():
    movie_list = prepopulate_movie_list()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_all_titles(movie_list)
        elif choice == "2":
            new_movie_title = input("Enter the new movie title: ")
            add_title(movie_list, new_movie_title)
        elif choice == "3":
            try:
                index_to_delete = int(input("Enter the index of the movie to delete: "))
                delete_title(movie_list, index_to_delete)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
