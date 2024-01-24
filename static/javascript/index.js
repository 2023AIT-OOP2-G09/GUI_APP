// 曜日の定義
const week = ["日", "月", "火", "水", "木", "金", "土"];

// 今日の日付
var today = new Date();

// 表示用の日付
var showDate = new Date(today.getFullYear(), today.getMonth(), 1);

// 表示された時


// カレンダーの表示
function showCalendar(date) {
  // 年
  var year = date.getFullYear();
  // 月
  var month = date.getMonth() + 1;

  // ヘッダーの年月に表示する文字列
  var showDateStr = year + "年 " + month + "月";

  // ヘッダーの年月部分に埋め込み
  document.querySelector('#year_month_label').innerHTML = showDateStr;

  // カレンダーテーブルを作成する（HTMLが返却される）
  var calendarTable = createCalendarTable(year, month);

  // カレンダー表示部分に埋め込み
  document.querySelector('#calendar_body').innerHTML = calendarTable;
}

// カレンダーテーブルの作成
function createCalendarTable(year, month) {
  // HTML用の変数
  var _html = '';

  // tableタグ
  _html += '<table class="calendar_tbl">';

  // テーブルのヘッダー（曜日）
  _html += '<tr>';
  for (var i = 0; i < week.length; i++) {
    _html += "<th>" + week[i] + "</th>";
  }
  _html += '</tr>';

  // ---------------------

  // 表示するカレンダー年月の1日の曜日を取得
  var startDayOfWeek = new Date(year, month - 1, 1).getDay();

  // 日付
  var countDay = 0;

  // 月の末日
  var monthOfEndDay = new Date(year, month, 0).getDate();

  // 6行分繰り返し
  for (var i = 0; i < 6; i++) {
    _html += '<tr>';

    // 7列（曜日の数）分繰り返し
    for (var j = 0; j < week.length; j++) {
      // １行目で開始曜日と同じ場合
      if (i == 0 && j == startDayOfWeek) {
        // 日付+1
        countDay++;

        // 今日の日付のセルに"today"クラスを適用
        if (countDay === today.getDate() && month === today.getMonth() + 1) {
          _html += '<td class="with_date today">' + countDay + '</td>';
        } else {
          _html += '<td class="with_date">' + countDay + '</td>';
        }
      }
      // 日付が0以外で、日付が末日より小さい場合
      else if (countDay != 0 && countDay < monthOfEndDay) {
        // 日付+1
        countDay++;

        // 今日の日付のセルに"today"クラスを適用
        if (countDay === today.getDate() && month === today.getMonth() + 1) {
          _html += '<td class="with_date today">' + countDay + '</td>';
        } else {
          _html += '<td class="with_date">' + countDay + '</td>';
        }
      } else {
        // tdタグ（日付無しが分かるようにクラス属性に"no_date"を設定）
        _html += '<td class="no_date"></td>';
      }
    }
    _html += '</tr>';
  }

  _html += '</table>';

  // 組み立てたHTMLを返却
  return _html;
}

// 前年
function prev_year() {
  // 表示用の日付の年-1を設定
  showDate.setFullYear(showDate.getFullYear() - 1);
  // カレンダーの表示（引数には表示用の日付を設定）
  showCalendar(showDate);
  renderScheduleData();
}

// 前月
function prev_month() {
  // 表示用の日付の月-1を設定
  showDate.setMonth(showDate.getMonth() - 1);
  // カレンダーの表示（引数には表示用の日付を設定）
  showCalendar(showDate);
  renderScheduleData();
}

// 今日
function now_month() {
  // 表示用の日付に今日の日付を設定
  showDate = new Date();
  // カレンダーの表示（引数には表示用の日付を設定）
  showCalendar(showDate);
  renderScheduleData();
}

// 来月
function next_month() {
  // 表示用の日付の月+1を設定
  showDate.setMonth(showDate.getMonth() + 1);
  // カレンダーの表示（引数には表示用の日付を設定）
  showCalendar(showDate);
  renderScheduleData();
}

// 来年
function next_year() {
  // 表示用の日付の年+1を設定
  showDate.setFullYear(showDate.getFullYear() + 1);
  // カレンダーの表示（引数には表示用の日付を設定）
  showCalendar(showDate);
  renderScheduleData();
}


// スケジュールデータの取得
async function fetchScheduleData() {
  try {
    const response = await fetch('/fetch_schedule');
    const scheduleData = await response.json();
    return scheduleData;
  } catch (error) {
    console.error('Error fetch:', error);
    return [];
  }
}

// スケジュールデータの表示
// スケジュールデータの表示
async function renderScheduleData() {
  try {
    const scheduleData = await fetchScheduleData();
    const currentYear = showDate.getFullYear();
    const currentMonth = showDate.getMonth() + 1;

    scheduleData.forEach(schedule => {
      const scheduleYear = new Date(schedule.date).getFullYear();
      const scheduleMonth = new Date(schedule.date).getMonth() + 1;

      // 年と月が一致する場合のみ表示
      if (currentYear === scheduleYear && currentMonth === scheduleMonth) {
        const day = new Date(schedule.date).getDate();
        const cells = document.querySelectorAll('.with_date');

        cells.forEach(cell => {
          if (parseInt(cell.innerText) === day) {
            const scheduleElement = document.createElement('div');
            scheduleElement.className = 'schedule-info';
            scheduleElement.innerHTML = schedule.schedule;

            // Remove existing schedule-info div
            const existingScheduleElement = cell.querySelector('.schedule-info');
            if (existingScheduleElement) {
              existingScheduleElement.remove();
            }

            cell.appendChild(scheduleElement);
          }
        });
      }
    });
  } catch (error) {
    console.error('Error rendering schedule data:', error);
  }
}

// 表示された時
window.onload = function () {
  showCalendar(showDate);
  renderScheduleData(); // スケジュールデータの取得と表示
};