// feather.replace()

// JavaScript kısmı

// Veri çekme işlemini belirli aralıklarla tekrarlayalım (örneğin, her 5 saniyede bir)


// window.onload = function () {
//     const eventSource = new EventSource("api_serial/");
//     eventSource.onmessage = async function (event) {
//         try {
//             console.log("event", event);
//             const data = JSON.parse(event.data);
//             console.log("data", data);
//             // Elementleri güncelle
//             // Veri başarıyla çekilirse, HTML elementlerini güncelle
//             document.getElementById('population').innerText = `${data.analog_value}%`;
//             document.getElementById('oxygen').innerText = `${data.air_quality}%`;
//             document.getElementById('co2').innerText = `${data.air_quality}%`; // CO2 için API'dan gelen veri bilinmediği için air_quality kullanıldı
//             document.getElementById('humidity').innerText = `${data.humidity}%`;
//             document.getElementById('temperature-environment').innerText = `${data.temperature}°C`;
//             document.getElementById('temperature-water').innerText = `${data.water_temperature}°C`;
//         } catch (error) {
//             console.error("try/catch:", error);
//         };
//     }

//     eventSource.onerror = function (error) {
//         // Eğer bir hata olursa, konsola yazdır
//         console.error('API ile iletişimde bir hata oluştu:', error);
//         eventSource.close();
//     };
// };


// setInterval(() => {
//     // fetch API ile veriyi çekiyoruz
//     fetch('/api_serial/')
//         .then(response => response.json())
//         .then(data => {
//             console.log(data)
//             // Veri başarıyla çekilirse, HTML elementlerini güncelle
//             document.getElementById('population').innerText = `${data.analog_value}%`;
//             document.getElementById('oxygen').innerText = `${data.air_quality}%`;
//             document.getElementById('co2').innerText = `${data.air_quality}%`; // CO2 için API'dan gelen veri bilinmediği için air_quality kullanıldı
//             document.getElementById('humidity').innerText = `${data.humidity}%`;
//             document.getElementById('temperature-environment').innerText = `${data.temperature}°C`;
//             document.getElementById('temperature-water').innerText = `${data.water_temperature}°C`;
//         })
//         .catch(error => {
//             // Eğer bir hata olursa, konsola yazdır
//             console.error('API ile iletişimde bir hata oluştu:', error);
//         });
// }, 2000); // 5000 milisaniye (5 saniye) aralıkla
