function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else if (this.status === 400) {
                document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
            } else {
                document.getElementById("system_response").innerHTML = "Server error. Please try again later.";
            }
        }
    };

    // Make sure the URL starts with a slash to reference Flask route
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
