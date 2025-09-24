let mtk = 85;
let inggris = 90;
let ipa = 78;

let nilairatarata = (mtk + inggris + ipa)/3;

console.log(`Siswa ini memiliki nilai rata rata: ${nilairatarata}`);
console.log(`Tipe data dari nilai rata rata adalah: ${typeof nilairatarata}`);

let statuskelulusan;
if (nilairatarata >= 80) {
    statuskelulusan = "Lulus";
} else {
    statuskelulusan = "Tidak Lulus";
}

console.log(`Status kelulusan siswa ini adalah: ${statuskelulusan}`)