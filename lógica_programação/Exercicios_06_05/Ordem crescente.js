var A = 15;
var B = 256;
var C = 242;
if ((A > B) && (A > C)) {
  if (B > C) {
    console.log(A);
    console.log(B);
    console.log(C);
  } else {
    console.log(A);
    console.log(C);
    console.log(B);
  }
}
if ((B > A) && (B > C)) {
  if (A > C) {
    console.log(B);
    console.log(A);
    console.log(C);
  } else {
    console.log(B);
    console.log(C);
    console.log(A);
  }
}
if ((C > A) && (C > B)) {
  if (B > A) {
    console.log(C);
    console.log(B);
    console.log(A);
  } else {
    console.log(C);
    console.log(A);
    console.log(B);
  }
}