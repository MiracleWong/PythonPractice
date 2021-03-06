import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def hello():
    click.echo('Hello World!')


# yes parameters
def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')


@click.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def dropdb2():
    click.echo('Dropped all tables!')


if __name__ == '__main__':
    dropdb2()
