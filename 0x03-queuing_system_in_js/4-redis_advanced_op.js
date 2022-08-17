import redis from "redis";
const client = createClient();
client
    .on("error", (error) => {
        console.log(`Redis client not connected to the server: ${error}`);
    })
    .on("ready", () => {
        console.log("Redis client connected to the server");
    });

const keyName = "olbertonSchools";
const values = {
    Portland: 50,
    "Seattle ": 80,
    "New York ": 20,
    Bogota: 20,
    "Cali ": 40,
    Paris: 2,
};
for (const [key, value] of Object.entries(values)) {
    client.hset(keyName, key, value, (error, reply) => {
        redis.print(`Reply: ${reply}`);
    });
}
client.hgetall(keyName, (error, object) => {
    console.log(object);
});