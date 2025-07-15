const num = [1234, 7421, -714, -7923, 166, -983, 642];
const result = num.filter(divisivel);
console.log(result)
function divisivel(num) {
 return num % 6==0;
}
