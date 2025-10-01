function hitungHargaAkhir(totalBelanja) {
    let diskon = 0;

    if (totalBelanja > 1000000) {
        diskon = 0.15;  
    } else if (totalBelanja > 500000) {
        diskon = 0.10;  
    } else {
        diskon = 0;     
    }

    let hargaAkhir = totalBelanja - (totalBelanja * diskon);
    return hargaAkhir;
}


console.log(hitungHargaAkhir(400000));  
console.log(hitungHargaAkhir(600000));  
console.log(hitungHargaAkhir(1500000)); 
