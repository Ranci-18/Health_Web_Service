let uniqueId = localStorage.getItem("uniqueId");

if (!uniqueId) {
    generateUniqueId();
} else {
	clearUniqueId();
}

function generateUniqueId () {
    uniqueId = generateRadomId();
    localStorage.setItem("uniqueId", uniqueId);
    document.getElementById("uniqueIdOutput").textContent = uniqueId;

    function generateRadomId () {
        return Math.random().toString(36).substring(2, 8);
    }
}

function clearUniqueId() {
    localStorage.removeItem("uniqueId");
    document.getElementById("uniqueIdOutput").textContent = "";
}

window.onload = function () {
    document.getElementById("uniqueIdOutput").textContent = uniqueId;
}
