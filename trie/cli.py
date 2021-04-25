import click
import requests


class Context:
    def __init__(self, word, server):
        self.word = word
        self.server = server


@click.group()
@click.option('-w', '--word', type=str, help='Input word')
@click.option('-s', '--server', envvar='TRIE_SERVER', default='http://54.177.45.15:8080', help='Server')
@click.pass_context
def cli(ctx, word, server):
    """Welcome to My Trie System"""
    ctx.obj = Context(word, server)


@cli.command()
@click.pass_context
def add(ctx):
    """Add word"""
    response = requests.post(ctx.obj.server+'/add',
                             params={'word': ctx.obj.word})
    output = response.json()['output']
    click.echo(output)


@cli.command()
@click.pass_context
def delete(ctx):
    """Delete word"""
    response = requests.post(ctx.obj.server+'/delete',
                             params={'word': ctx.obj.word})
    output = response.json()['output']
    click.echo(output)


@cli.command()
@click.pass_context
def search(ctx):
    """Search word"""
    response = requests.get(ctx.obj.server+'/search',
                            params={'word': ctx.obj.word})
    output = response.json()['output']
    click.echo(output)


@cli.command()
@click.pass_context
def autocomplete(ctx):
    """Autocomplete suggestions"""
    response = requests.get(ctx.obj.server+'/autocomplete',
                            params={'word': ctx.obj.word})
    output = response.json()['output']
    click.echo(output)


@cli.command()
@click.pass_context
def display(ctx):
    """Display trie"""
    response = requests.get(ctx.obj.server+'/display')
    output = response.json()['output']
    click.echo(output)


if __name__ == '__main__':
    cli()
