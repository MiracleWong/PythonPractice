import click
# other prefix
@click.command()
@click.option('+w/-w')
def chmod(w):
    click.echo('writable=%s' % w)


if __name__ == '__main__':
    chmod()
