// カレンダーのセルがクリックされたときに呼び出される関数
async function handleCellClick(event) {
    // クリックされた要素がtdであるかを確認
    if (event.target.tagName === 'TD') {
        // クリックされた日付のスケジュールを取得
        const day = event.target.textContent;
        if (day) {
            // スケジュールデータの取得
            const scheduleData = await fetchScheduleData();

            // クリックされた日付に対応するスケジュールをフィルタリング
            const currentDate = new Date();
            const currentYear = currentDate.getFullYear();
            const currentMonth = currentDate.getMonth() + 1; // 月は0-indexedなので1を加える
            const schedulesForDay = scheduleData.filter(schedule => {
                const scheduleDate = new Date(schedule.date);
                const scheduleYear = scheduleDate.getFullYear();
                const scheduleMonth = scheduleDate.getMonth() + 1;
                const scheduleDay = scheduleDate.getDate();
                return scheduleYear === currentYear && scheduleMonth === currentMonth && scheduleDay === parseInt(day);
            });

            // 予定が存在する場合は表示
            if (schedulesForDay.length > 0) {
                // 遷移先URLの生成
                const url = `/index/to?day=${encodeURIComponent(day)}&schedule=${encodeURIComponent(JSON.stringify(schedulesForDay))}`;
                // 遷移
                window.location.href = url;
            }
        }
    }
}