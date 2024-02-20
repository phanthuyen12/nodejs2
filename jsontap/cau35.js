function nhapChuoi(callback) {
    // Giả sử rằng bạn sử dụng một cách nào đó để nhập chuỗi từ người dùng
    let chuoi = prompt("Nhập vào một chuỗi:");
    // Gọi hàm callback và truyền vào chiều dài của chuỗi
    callback(chuoi.length);
}

// Hàm callback để in ra chiều dài của chuỗi
function inChieuDaiChuoi(chieuDai) {
    console.log("Chiều dài của chuỗi là:", chieuDai);
}

// Sử dụng hàm nhapChuoi và truyền vào hàm callback inChieuDaiChuoi
nhapChuoi(inChieuDaiChuoi);
