import calendar

def create_links(year, month, filename):
    # Get the last day of the month
    _, last_day = calendar.monthrange(year, month)

    with open(filename, "w") as file:
        # Create links for each day of the month
        for day in range(1, last_day + 1):
            date_str = f"{year:04d}/{month:02d}/{day:02d}"
            link = f"https://gigazine.net/news/{date_str}/"
            file.write(f"<a href='{link}' target='_blank'>{link}</a><br>\n")

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    filename = input("Enter the filename (e.g., links.html): ")

    create_links(year, month, filename)
