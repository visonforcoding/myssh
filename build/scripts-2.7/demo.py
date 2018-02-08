# coding=utf-8
import click
import subprocess

#subprocess.call(['ssh', '-p', '62130', 'vison@dev.huolala.cn'])

config = {
    1: {'port': '62130', 'host': 'vison@dev.huolala.cn'}
}


@click.command()
def main():
    click.echo(click.style('welcome login ssh server by vison .v1.0', fg='red'))
    click.echo(click.style('可选的服务列表:', fg='red'))
    click.echo(click.style('   1) dev.huolala.cn', fg='white'))
    value = click.prompt('输入要登录的host', type=int)
    if value in config:
        subprocess.call(['ssh','-p',config[value]['port'],config[value]['host']])
    else:
        click.echo(click.style('输入有误',fg='red'))


if __name__ == '__main__':
    main()
