const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();

const reserveSeat = async (number) => {
  await client.setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const seats = await getAsync('available_seats');
  return parseInt(seats);
};

reserveSeat(50); // Set initial available seats to 50
let reservationEnabled = true;

const kue = require('kue');
const queue = kue.createQueue();

queue.on('error', (err) => {
  console.error('Kue Error:', err);
});

const express = require('express');
const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      console.error('Error saving job:', err);
      res.json({ status: 'Reservation failed' });
    } else {
      console.log('Job enqueued:', job.id);
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let currentSeats = await getCurrentAvailableSeats();
    if (currentSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      currentSeats--;
      await reserveSeat(currentSeats);
      if (currentSeats === 0) reservationEnabled = false;
      console.log(`Seat reservation job ${job.id} completed`);
      done();
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});



