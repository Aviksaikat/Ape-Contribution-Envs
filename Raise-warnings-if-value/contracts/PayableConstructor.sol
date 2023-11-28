// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract PayableConstructor {

    address public owner;
    constructor() payable {
        owner = msg.sender;
    }

    function getOwner() external view returns(address){
        return owner;
    }

}