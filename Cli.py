import random
import click

from giphyAPI import GiphyAPI

class GiphyCLI:

    @click.group()
    def gif():
        print("hello from giphy cli!")

    @gif.command()
    @click.option("--count", default=5, help="Number of gifs to print.")
    @click.option(
        "--markdown",
        is_flag=True,
        show_default=True,
        default=False,
        help="Prints in markdown's image format",
    )
    @click.option(
        "--lucky",
        is_flag=True,
        show_default=True,
        default=False,
        help="Prints a random gif",
    )
    def trending(count, markdown, lucky):
        print("trending subcommand called.")
        giphy_api = GiphyAPI()
        gifs = giphy_api.get_trending_gifs()  # fixed get_trending_gifs

        if lucky:
            # Directly choosing a random gif from the list
            random_gif = random.choice(gifs['data'])  # Corrected variable name
            url = random_gif["url"]  # Assuming this is the correct key
            md_url = random_gif["images"]["original"]['url']
            title = random_gif.get("title", "No title")
            if markdown:
                print(f"![{title}]({md_url})")
            else:
                print(f"{title} ({url})")
        else:
            number = 1
            for gif_data in gifs["data"][:count]:
                url = gif_data["url"]  # Assuming this is the correct key
                md_url = gif_data["images"]["original"]["url"]
                title = gif_data.get("title", "No title")
                if markdown:
                    print(f"{number}) ![{title}]({md_url})")
                else:
                    print(f"{number}) {title} ({url})")
                number += 1

        
    @gif.command()
    # set count to 5 by default if not specified
    @click.option("--count", default = 5 , help = "Number of gifs to print.")
    @click.option(
        "--markdown",
        is_flag=True,
        show_default=True,
        default=False,
        help="Prints gifs in markdown format",
    )
    @click.option(
        "--lucky",
        is_flag=True,
        show_default=True,
        default=False,
        help="Prints a random gif",
    )
    @click.argument("searchTerm")
    # params for command
    def search(count, markdown, lucky, searchterm):
        print("search subcommand called.")
        giphy_api = GiphyAPI()
        gifs = giphy_api.get_SearchGifs(searchterm)
        if lucky:
            random_gif = random.choice(gifs["data"])
            url = random_gif["bitly_gif_url"]
            md_url = random_gif["images"]["original"]["url"]
            title = random_gif["title"]
            if markdown:
                print(f"[{title}]({md_url})")
            else:
                print(f"{title} ({url})")
        else:
            number = 1
            for gif_data in gifs["data"][:count]:
                url = gif_data["bitly_gif_url"]
                md_url = gif_data["images"]["original"]["url"]
                title = gif_data["title"]
                if markdown:
                    print(f"{number}) ![{title}]({md_url})")
                else:
                    print(f"{number}) {title} ({url})")
                number += 1 