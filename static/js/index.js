$(function () {
    // 健康打卡
    let date = new Date();
    let today = getToday(date);
    let year = date.getFullYear();
    let month = date.getMonth();
    $("#dk-time").text(`最近打卡时间：${today} 00:15`);

    // 健康码
    $("#jkm-time").text(`${today} 06:30`)

    // 核酸检测
    let day = 24 * 60 * 60000
    $("#hs-time").text(`${getToday(new Date(date.getTime() - day))} 23:17`);

    // 有效期
    let beginDate = (new Date(date.getTime() - 11 * day)).toISOString().split('T')[0];
    let lastDay = (new Date(year, month + 1, 0)).toLocaleDateString('zh').split("/")[2];
    let endDate = `${year}-${p(month + 1)}-${lastDay}`;
    $("#blue-code-span").text(`有效期：${beginDate} - ${endDate}`)

    // 蓝码
    let text = $("#blue-code-text").val();
    if (!text) {
        alert("蓝码数据获取失败");
    }

    $('#output').qrcode({
        render: "table",
        width: 180,
        height: 180,
        text: text,
        render: "canvas",
        foreground: "#1E90FF",
        background: "#FFF",
        style: "border: 4px solid #038aff; padding: 5px;"
    });

    setInterval(() => {
        let time = new Date();
        let mon = p(time.getMonth() + 1);
        let d = p(time.getDate());
        let h = p(time.getHours());
        let m = p(time.getMinutes());
        let s = p(time.getSeconds());
        $("#div_timer").text(`${mon}月${d}日 ${h}:${m}:${s}`)
    }, 1000);
})


/**
 * 为数字补前导零
 * @param {number} s 数字，从 0-11
 * @returns 补零后的数字字符串
 */
function p(s) {
    return s < 10 ? '0' + s : '' + s;
}

/**
 * 获取当前日期
 * @param {Date} date 日期
 * @returns 当前日期，不包含年份，格式为 `MM-DD`
 */
function getToday(date) {
    return `${p(date.getMonth() + 1)}-${p(date.getDate())}`;
}