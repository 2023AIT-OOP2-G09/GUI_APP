function showMessage() {
    // HTMLからデータを取得
    let date = document.getElementById('date').value;
    let schedule = document.getElementById('schedule').value;

    // データをJSON形式に変換
    let dataFromHTML = {
        date: date,
        schedule: schedule
    };

    // JSONを表示
    alert(JSON.stringify(dataFromHTML));
    // 既存のJSONファイルを読み込む
    let jsonData = JSON.parse(fs.readFileSync('schedule.json', 'utf8'));

    // JSONに新たなデータを追加
    jsonData.newData = dataFromHTML;

    // JSONを再度ファイルとして保存
    fs.writeFileSync('schedule.json', JSON.stringify(jsonData));

}