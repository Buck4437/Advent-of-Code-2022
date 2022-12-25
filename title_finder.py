from bs4 import BeautifulSoup
import requests


def main():
    with open("titles.txt", "w") as f:
        for i in range(1, 26):
            r = requests.get(f"https://adventofcode.com/2022/day/{i}")
            status_code = r.status_code
            print("Status code", status_code)
            if status_code != 200:
                return
            soup = BeautifulSoup(r.content, "html.parser")
            tags = soup.select("h2")
            for tag in tags:
                f.write(tag.text.strip().strip("- "))
                f.write("\n")


main()
