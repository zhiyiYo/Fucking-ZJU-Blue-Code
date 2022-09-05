$(function () {
    // 健康打卡
    let date = new Date();
    $("#dk-time").text(`最近打卡时间：${p(date.getMonth() + 1)}-${p(date.getDate())} 00:15`);

    // 核酸检测
    let day = 24 * 60 * 60000
    date.setTime(date.getTime() - day);
    $("#hs-time").text(`${p(date.getMonth() + 1)}-${p(date.getDate())} 16:15`);

    // 有效期
    let begin_time = (new Date(date.getTime() - 11 * day)).toISOString().split('T')[0];
    let end_time = (new Date(date.getTime() + 12 * day)).toISOString().split('T')[0];
    $("#blue-code-span").text(`有效期：${begin_time} - ${end_time}`)

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


function p(s) {
    return s < 10 ? '0' + s : s;
}