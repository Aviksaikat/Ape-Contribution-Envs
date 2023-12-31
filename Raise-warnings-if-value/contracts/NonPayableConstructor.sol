// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract NonPayableConstructor {

    address public owner;
    constructor() {
        owner = msg.sender;
    }

    function getOwner() external view returns(address){
        return owner;
    }

}