import click
import setting

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo("Hello, %s!" % name)
        click.echo(setting.area_info["quz"]["vsw_info"][0])
        click.echo(setting.area_info["quz"]["name_zh_CN"])


if __name__ == '__main__':
    hello()
