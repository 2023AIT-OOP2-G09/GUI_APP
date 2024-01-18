// Given JSON data
/*const jsonData = [
    {
      "date": "2024/01/11",
      "schedule": "こんにちは",
      "time": "0:00"
    },
    {
      "date": "2024/01/12",
      "schedule": "物理実習",
      "time": "13:00"
    },
    {
      "date": "2024/01/13",
      "schedule": "プログラミング実習",
      "time": "14:00"
    },
    {
      "date": "2024/01/17",
      "schedule": "予定の追加（例）",
      "time": "0:00"
    },
    {
      "date": "2024/02/01",
      "schedule": "予定の追加（例２）",
      "time": "0:00"
    }
  ];

  // スケジュールアイテムを作成し、コンテナに追加する関数
function renderScheduleItems(data) {
    const container = document.getElementById('scheduleContainer');
  
    data.forEach(item => {
      const scheduleItem = document.createElement('div');
      scheduleItem.classList.add('schedule-item');
      scheduleItem.innerHTML = `<strong>日付:</strong> ${item.date}<br><strong>時間:</strong> ${item.time}<br><strong>スケジュール:</strong> ${item.schedule}`;
      container.appendChild(scheduleItem);
    });
  }
  
  // ファイルの読み込みに使用されている相対パスを修正
async function fetchDataAndRender() {
    try {
      const response = await fetch('schedule.json');
      const jsonData = await response.json();
      renderScheduleItems(jsonData);
    } catch (error) {
      console.error('データの取得エラー:', error);
    }
  }
  
  
  // ページ読み込み時にスケジュールアイテムをレンダリング
  window.addEventListener('load', function () {
    fetchDataAndRender();
  });*/
  // Given JSON data
  
  
function renderScheduleItems(data) {
  const container = document.getElementById('scheduleContainer');

  data.forEach(item => {
    const scheduleItem = document.createElement('div');
    scheduleItem.classList.add('schedule-item');
    scheduleItem.innerHTML = `<strong>Date:</strong> ${item.date}<br><strong>Time:</strong> ${item.time}<br><strong>Schedule:</strong> ${item.schedule}`;
    container.appendChild(scheduleItem);
  });
}

// Render schedule items on page load
window.addEventListener('load', function () {
  fetch("/getjson").then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // 取得したJSONデータを利用する
            console.log(data);
            const jsonData = data
            // ここで適切な処理を行う（例: 表示、変数への代入など）
            renderScheduleItems(jsonData);
            
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
});