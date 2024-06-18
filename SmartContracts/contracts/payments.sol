// SPDX-License-Identifier: MIT
// @Author: Bertan Berker
// @File: payments.sol
// This is a smart contract that handles the payments between the player and the house

pragma solidity ^0.8.2;


contract Payments {

    uint256 house_balance;
    uint256 player_balance;

    constructor(uint256 _house, uint256 _player) {
        house_balance = _house;
        player_balance = _player;

    }

    function addHouse(uint256 _money) public {
        house_balance += _money;
    }

    function addPlayer(uint256 _money) public {
        player_balance += _money;
    }

    function subHouse(uint256 _money) public {
        house_balance -= _money;
    }

    function subPlayer(uint256 _money) public {
        player_balance -= _money;
    }

    function getHouseBalance() public view returns (uint256) {
        return house_balance;
    }

    function getPlayerBalance() public view returns (uint256) {
        return player_balance;
    }

}