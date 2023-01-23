const express = require('express');
const mysql = require('mysql');
const cors = require('cors');

const app = express();

app.use(express.json());
app.use(cors())

const db = mysql.createConnection({
    user: 'root',
    host: 'localhost',
    password: 'Apravamthe@98',
    database: 'test',
});

app.post('/signup', (req, res) => {

    const username = req.body.username;
    const password = req.body.password;

    db.query("INSERT INTO users (username, password) VALUES (?, ?)", [username, password], (err, result) => {
        if (err) {
            console.log(err);
            res.send({ message: "Error while registering" })
        } else {
            console.log(result)
            res.send(result);
        }
    });
});

app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    db.query("SELECT * FROM users WHERE username = ? AND password = ?", [username, password], (err, result) => {
        if (err) {
            console.log(err);
        } else {
            if (result.length > 0) {
                res.send(result);
            } else {
                res.send({ message: "Wrong username/password combination" });
            }
        }
});
});

app.get('/adopt', (req, res) => {
    db.query("SELECT * FROM ANIMALS", (err, result) => {
        if (err) {
            console.log(err);
        } else {
            console.log(result)
            res.send(result);
        }
    })
    // res.send("Adopt")
    // console.log("Adopt")
}
)

app.listen(3001, () => {
    console.log("Server is running on port 3001");
})