const express = require("express");
const app = express();
app.use(express.json());
const swaggerUi = require("swagger-ui-express");
const swaggerJsdoc = require("swagger-jsdoc");

const PORT = 3000;
const students = [
    {
        id: 1,
        name: "Ahmed",
        age: 20,
    },
    {
        id: 2,
        name: "Sara",
        age: 21,
    },
];

app.get("/", (req, res) => {
    res.send("Hello World");
});

/**
 * @swagger
 * /students:
 *   get:
 *     summary: Get all students
 *     responses:
 *       200:
 *         description: List of students
 */
app.get("/students", (req, res) => {
    res.json(students);
});
/**
 * @swagger
 * /students:
 *   post:
 *     summary: Add a new student
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               id:
 *                 type: integer
 *               name:
 *                 type: string
 *               age:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Student added successfully
 */
app.post("/students", (req, res) => {
    const newStudent = req.body;

    students.push(newStudent);

    res.json({
        message: "Student added successfully",
        student: newStudent,
    });
});
/**
 * @swagger
 * /students/{id}:
 *   put:
 *     summary: Update a student
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *               age:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Student updated successfully
 *       404:
 *         description: Student not found
 */
app.put("/students/:id", (req, res) => {
    const id = parseInt(req.params.id);

    const student = students.find(student => student.id === id);

    if (!student) {
        return res.status(404).json({
            message: "Student not found",
        });
    }

    student.name = req.body.name;
    student.age = req.body.age;

    res.json({
        message: "Student updated successfully",
        student: student,
    });
});
/**
 * @swagger
 * /students/{id}:
 *   delete:
 *     summary: Delete a student
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Student deleted successfully
 *       404:
 *         description: Student not found
 */
app.delete("/students/:id", (req, res) => {
    const id = parseInt(req.params.id);

    const studentIndex = students.findIndex(student => student.id === id);

    if (studentIndex === -1) {
        return res.status(404).json({
            message: "Student not found",
        });
    }

    students.splice(studentIndex, 1);

    res.json({
        message: "Student deleted successfully",
    });
});

const options = {
    definition: {
        openapi: "3.0.0",
        info: {
            title: "Students API",
            version: "1.0.0",
            description: "Simple CRUD API using Express",
        },
    },
    apis: ["./index.js"],
};

const swaggerSpec = swaggerJsdoc(options);

app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});