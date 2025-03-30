const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 5000;

app.use(express.json());
app.use(cors());

// Ruta para calcular el IMC
app.post("/imc", (req, res) => {
    const { peso, altura } = req.body;
    if (!peso || !altura) {
        return res.status(400).json({ error: "Datos insuficientes" });
    }
    const imc = peso / (altura * altura);
    res.json({ imc: imc.toFixed(2) });
});

// Ruta para calcular el IGC
app.post("/igc", (req, res) => {
    const { peso, altura, edad, sexo } = req.body;
    if (!peso || !altura || !edad || !sexo) {
        return res.status(400).json({ error: "Datos insuficientes" });
    }
    const imc = peso / (altura * altura);
    const igc = sexo === "M"
        ? (1.2 * imc + 0.23 * edad - 16.2)
        : (1.2 * imc + 0.23 * edad - 5.4);
    res.json({ igc: igc.toFixed(2) });
});

// Ruta para calcular la TMB
app.post("/tmb", (req, res) => {
    const { peso, altura, edad, sexo } = req.body;
    if (!peso || !altura || !edad || !sexo) {
        return res.status(400).json({ error: "Datos insuficientes" });
    }
    const tmb = sexo === "M"
        ? (88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * edad))
        : (447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * edad));
    res.json({ tmb: tmb.toFixed(2) });
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
