async function predict() {

    let data = [
        Number(document.getElementById("preg").value),
        Number(document.getElementById("glucose").value),
        Number(document.getElementById("bp").value),
        Number(document.getElementById("skin").value),
        Number(document.getElementById("insulin").value),
        Number(document.getElementById("bmi").value),
        Number(document.getElementById("dpf").value),
        Number(document.getElementById("age").value)
    ];

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ data: data })
    });

    let result = await response.json();

    if (result.prediction === 1) {
        document.getElementById("result").innerText = "⚠️ High Risk of Diabetes";
    } else {
        document.getElementById("result").innerText = "✅ Low Risk";
    }
}