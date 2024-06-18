const Payments = artifacts.require("Payments");

contract("Payments", accounts => {
    let paymentsInstance;

    // Deploy the contract before each test
    before(async () => {
        paymentsInstance = await Payments.new(0, 0);
    });

    it("should have correct initial balances", async () => {
        let houseBalance = await paymentsInstance.getHouseBalance();
        let playerBalance = await paymentsInstance.getPlayerBalance();

        assert.equal(playerBalance.toString(), '0', "Initial player balance should be 0");
        assert.equal(houseBalance.toString(), '0', "Initial house balance should be 0");
    });

    it("should add to house balance correctly", async () => {
        await paymentsInstance.addHouse(100);
        let houseBalance = await paymentsInstance.getHouseBalance();

        assert.equal(houseBalance.toString(), '100', "House balance should be updated correctly");
    });

    it("should add to player balance correctly", async () => {
        await paymentsInstance.addPlayer(50);
        let playerBalance = await paymentsInstance.getPlayerBalance();

        assert.equal(playerBalance.toString(), '50', "Player balance should be updated correctly");
    });

    it("should subtract from house balance correctly", async () => {
        await paymentsInstance.subHouse(20);
        let houseBalance = await paymentsInstance.getHouseBalance();

        assert.equal(houseBalance.toString(), '80', "House balance should be decreased correctly");
    });

    it("should subtract from player balance correctly", async () => {
        await paymentsInstance.subPlayer(10);
        let playerBalance = await paymentsInstance.getPlayerBalance();

        assert.equal(playerBalance.toString(), '40', "Player balance should be decreased correctly");
    });
});
