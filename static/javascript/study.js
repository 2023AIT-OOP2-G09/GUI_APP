document.addEventListener("DOMContentLoaded", function () {
    // JSONデータ
    const jsonData = [
      {"date": "2024/01/09", "schedule": "こんにちは", "studyTime": 2},
      {"date": "2024/01/11", "schedule": "こんにちは", "studyTime": 3},
      {"date": "2024/01/12", "schedule": "物理実習", "studyTime": 4},
      {"date": "2024/01/13", "schedule": "プログラミング実習", "studyTime": 5},
      {"date": "2024/01/17", "schedule": "予定の追加（例）", "studyTime": 1},
      {"date": "2024/02/01", "schedule": "予定の追加（例２）", "studyTime": 2}
    ];//書き換え

    // 勉強時間データを処理して配列に変換
    const studyTimeData = jsonData.map(item => item.studyTime);

    // Chart.jsを使用して円グラフを描画
    const ctx = document.getElementById('pie-chart').getContext('2d');
    const pieChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: jsonData.map(item => item.schedule),
        datasets: [{
          data: studyTimeData,
          backgroundColor: [
            'red', 'blue', 'green', 'orange', 'purple', 'pink'
          ]
        }]
      },
      options: {
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              const dataIndex = tooltipItem.index;
              const label = data.labels[dataIndex];
              const studyTime = jsonData[dataIndex].studyTime;
              return `${label}: ${studyTime} hours`;
            }
          }
        }
      }
    });

    // 一番多い時間と勉強名を表示
    const maxIndex = studyTimeData.indexOf(Math.max(...studyTimeData));
    const maxLabel = jsonData[maxIndex].schedule;
    const maxStudyTime = studyTimeData[maxIndex];
    const chartLabel = document.getElementById('chart-label');
    chartLabel.innerHTML = `${maxLabel}<br>${maxStudyTime} hours`;

    // ホバー時のイベントリスナー
    document.getElementById('pie-chart').addEventListener('mousemove', function(event) {
      const activePoint = pieChart.getElementsAtEventForMode(event, 'nearest', {intersect: true}, false)[0];
      if (activePoint) {
        chartLabel.style.opacity = 1;
        chartLabel.style.top = `${activePoint.y}px`;
        chartLabel.style.left = `${activePoint.x}px`;
      } else {
        chartLabel.style.opacity = 0;
      }
    });
  });