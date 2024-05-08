import redis from 'redis';
const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}
