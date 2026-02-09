def famous_births(figures):
    sorted_figures = sorted(figures.items(), key=lambda x: x[1]['date_of_birth'])
    for key, data in sorted_figures:
        print(f"{data['name']} is a great scientist born in {data['date_of_birth']}.")

#test
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)