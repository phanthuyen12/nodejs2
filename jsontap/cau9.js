function daoNguocChuoi(chuoi) {
    return chuoi.split('').reverse().join('');
}

// Sử dụng hàm
let chuoi = "Hello, world!";
let chuoiDaoNguoc = daoNguocChuoi(chuoi);
console.log(chuoiDaoNguoc); // In ra "!dlrow ,olleH"
