const Payments = artifacts.require("Payments");

module.exports = function(deployer) {
    const initialHouseBalance = 1000000
    const initialPlayerBalance = 10000
    deployer.deploy(Payments, initialHouseBalance, initialPlayerBalance);
};