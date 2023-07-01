function doCall(a){
    return new Promise((f) => {
        f(a*2);
    });
}

function test(){
    let i = 10;
    doCall(i).then((a) => {
        i=a;
    });
    console.log(i);
}