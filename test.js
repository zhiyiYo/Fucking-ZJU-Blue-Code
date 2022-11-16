let date = new Date();
date = new Date(date.getFullYear(), 6, 0);
console.log(date.toLocaleDateString('zh').split("/")[2]);