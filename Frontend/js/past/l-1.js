console.log("hello from l-1.js");
let a=25;

{
    let b=90;
    console.log(b)
}
{
    let n=90;
    console.log(n);
}
{
    const c=100;
    console.log(c);
}
{
    const c=0;
    console.log(c);
}
console.log(typeof a);
const student={
    name:"John",
    age:22,
    isGraduated:true

}
console.log("5==25:",5==25);
let x=9;
let z=10;

let cond1=x<z;
let cond2=x===z;
console.log("cond1 && cond2:",cond1 && cond2);

let color;
let mode="dark";
if(mode=="dark"){
    color="black";
}else{
    color="white";
}
console.log("color:",color);

let res=x>5?"Children":"Adult";
console.log("res:",res);
let name=prompt("Enter your name:");
console.log("name:",name);
let num=prompt("Enter a number:");
console.log("num:",num);
if(num%5==0){
    console.log("is divisible by 5");
}else{
    console.log("is not divisible by 5");
}

for(let i=0;i<5;i++){
    console.log("i:",i);
}   
for(let key in student){
    console.log("key:",key,"value:",student[key]);
}
//generating uss=ername for the input name
let username="@";
console.log("username:",username+name.toLowerCase());
let res1=prompt("want this or not (yes/no):");
if(res1=="yes"){
    console.log("username accepted:",username+name.toLowerCase());
}else{
    if(prompt("want to change (yes/no):")=="yes"){
        let num=prompt("Enter number to add at last:");
        console.log("new username:",username+name.toLowerCase()+num);

    }
}