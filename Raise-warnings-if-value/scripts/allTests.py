#!/usr/bin/python3
from ape import project, accounts

user = accounts[1]
user.set_autosign(True)
user.balance += int(100e18)

def test_PayableConstructor():
    pc = project.PayableConstructor.deploy(sender=user, value="1 ether")

    print(pc.getOwner(sender=user, value= "1 ether"))

def test_NonPayableConstructor():
    #npc = project.NonPayableConstructor.deploy(sender=user, value="1 ether")
    npc = user.deploy(project.NonPayableConstructor, value="1 ether")
    
    print(npc.getOwner())

def main():
    test_PayableConstructor()
    #test_NonPayableConstructor()
    