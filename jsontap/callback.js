function xuLyso(so, callback ){
    let ketqua = so *2;
    callback(ketqua);
}
function inketqua(ketqua){
    console.log('kết quả xử lý là :'+ketqua);
}
function kettrachanle(ketqua){
    if(ketqua %2 ==0){
        console.log("kết quả là 1 số chẳn")
    }else{
        console.log("kết quả 1 số lẻ")
    }
}
function kiemtraAmduong(ketqua){
    if(ketqua >=0){
        console.log(" kết quả số dương");

    }else{
        console.log("kết quả là 1 số âm");
    }
}
xuLySo(5, inketqua); // In ra: Kết quả xử lý là: 10
