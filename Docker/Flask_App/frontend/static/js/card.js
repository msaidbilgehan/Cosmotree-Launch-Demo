// feather.replace()

// JavaScript kısmı

// Veri çekme işlemini belirli aralıklarla tekrarlayalım (örneğin, her 5 saniyede bir)


window.onload = function () {
    const eventSource = new EventSource("api_serial/");
    eventSource.onmessage = async function (event) {
        try {
            const data = JSON.parse(event.data);
            // Elementleri güncelle
            // Veri başarıyla çekilirse, HTML elementlerini güncelle
            document.getElementById('population').innerText = `${data.population} %`;
            document.getElementById('oxygen').innerText = `${data.oxygen} %`;
            document.getElementById('co2').innerText = `${data.co2} %`;
            document.getElementById('humidity').innerText = `${data.humidity} %`;
            document.getElementById('temperature-environment').innerText = `${data.temperature_environment} °C`;
            document.getElementById('temperature-water').innerText = `${data.temperature_water} °C`;

            document.getElementById('producing-o2').innerText = `${data.producing_o2} gr`;
            document.getElementById('carbon-footprint-recycle').innerText = `${data.carbon_footprint_recycle} gr`;

        } catch (error) {
            console.error("try/catch:", error);
        };
    }
}
