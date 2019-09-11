import click


# unicode 是 Python2 的写法
@click.command()
# @click.option('--item', type=click.Tuple([str, int]))
@click.option('--item', type=(str, int))
def putitem(item):
    click.echo('name=%s id=%d' % item)


if __name__ == '__main__':
    putitem()
