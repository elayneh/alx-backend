import kue from "kue";

const queue = kue.createQueue();

const jobdata = {
    phoneNumber: "9165219225",
    message: "here is your code",
};

const job = queue
    .create("push_notification_code", jobdata)
    .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
    })
    .on("complete", () => {
        console.log("Notification job completed");
        job.on("failed", () => console.log("Notification job failed"));
    });