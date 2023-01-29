from brownie import tricrypto, accounts
import click

def get_signer():
    account = click.prompt("signer", type=click.Choice(accounts.load()))
    return accounts.load(account)

def main():
    acct = get_signer()
    tricrypto.deploy({'from': acct}, publish_source=True)