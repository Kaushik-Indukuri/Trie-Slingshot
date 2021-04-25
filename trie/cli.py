import click
import requests


class Context:
    def __init__(self, word, server):
        self.word = word
        self.server = server


@click.group()
@click.option('-w', '--word', type=str, help='Input word')
@click.option('-s', '--server', envvar='TRIE_SERVER', default='http://13.52.104.70:8080', help='Server')
@click.pass_context
def cli(ctx, word, server):
    """Welcome to My Trie System"""
    ctx.obj = Context(word, server)


@cli.command()
@click.pass_context
def add(ctx):
    """Add word"""
    response = requests.post(f'%s/add' % ctx.obj.server,
                             params={'word': ctx.obj.word})
    click.echo(response.json()["output"])


@cli.command()
@click.pass_context
def delete(ctx):
    """Delete word"""
    response = requests.post(f'%s/delete' %
                             ctx.obj.server, params={'word': ctx.obj.word})
    click.echo(response.json()["output"])


@cli.command()
@click.pass_context
def search(ctx):
    """Search word"""
    response = requests.get(f'%s/search' %
                            ctx.obj.server, params={'word': ctx.obj.word})
    click.echo(response.json()["output"])


@cli.command()
@click.pass_context
def autocomplete(ctx):
    """Autocomplete suggestions"""
    response = requests.get(f'%s/autocomplete' %
                            ctx.obj.server, params={'word': ctx.obj.word})
    click.echo(response.json()["output"])


@cli.command()
@click.pass_context
def display(ctx):
    """Display trie"""
    response = requests.get(f'%s/display' % ctx.obj.server)
    click.echo(response.json()["output"])


if __name__ == '__main__':
    cli()
