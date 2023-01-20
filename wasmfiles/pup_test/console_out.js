

/*
const puppeteer = require('puppeteer');
// print process.argv
process.argv.forEach(async function (val, index, array) {
    if (index == 2)
    {
    const browser = await puppeteer.launch();
    const page =await browser.newPage();
//page.on('console', message =>console.log(`${message.type().substr(0, 3).toUpperCase()} ${message.text()}`)).on('pageerror', ({ message }) => console.log(message)).on('response', response =>console.log(`${response.status()} ${response.url()}`)).on('requestfailed', request =>console.log(`${request.failure().errorText} ${request.url()}`));
    page.on('console', msg => console.log('PAGE LOG:', msg.text));    
//page.on('console', async e => { const args = await Promise.all(e.args().map(a => a.jsonValue()));console[e.type() === 'warning' ? 'warn' : e.type()](...args); });
    const metrics = await page.metrics();
    console.log("Time stamps: "+metrics.Timestamp) ;
    console.log("Script duration: "+metrics.ScriptDuration) ;
    console.log("Task duration: "+metrics.TaskDuration);
    console.log("__________________________________________________")
    //console.info(metrics);
    await page.goto("http://0.0.0.0:8000/"+val);
    //await page.screenshot( { path: "test_pic.png"});
    await browser.close();
    }
  });

async function main() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    page.on('console', message =>console.log(`${message.type().substr(0, 3).toUpperCase()} ${message.text()}`)).on('pageerror', ({ message }) => console.log(message)).on('response', response =>console.log(`${response.status()} ${response.url()}`)).on('requestfailed', request =>console.log(`${request.failure().errorText} ${request.url()}`));
    page.on('console', msg => console.log('PAGE LOG:', msg.text));    
    page.on('console', async e => { const args = await Promise.all(e.args().map(a => a.jsonValue()));console[e.type() === 'warning' ? 'warn' : e.type()](...args); });
    const metrics = await page.metrics();
    console.log("Time stamps: "+metrics.Timestamp) ;
    console.log("Script duration: "+metrics.ScriptDuration) ;
    console.log("Task duration: "+metrics.TaskDuration);
    console.log("__________________________________________________")
    console.info(metrics);
    await page.goto('http://0.0.0.0:8000/sum.html');
    console.log("End_____________________");
    await browser.close();
  }
  main();

  process.argv.forEach( async function (val, index , array ) {
    console.log(index + ':' + val) ; 
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://0.0.0.0:8000/sum.html');
   // page.on('console', msg => console.log('PAGE LOG:', msg.text));    
    page.on('console', async e => { const args = await Promise.all(e.args().map(a => a.jsonValue()));console[e.type() === 'warning' ? 'warn' : e.type()](...args); });
    const metrics = await page.metrics();
    console.log("Time stamps: "+metrics.Timestamp) ;
    console.log("Script duration: "+metrics.ScriptDuration) ;
    console.log("Task duration: "+metrics.TaskDuration);
    console.log("__________________________________________________");
    await browser.close();
 });*/
  

 /*
 page.on('console', async e => { c only works the browser does not get closed, exept that sometimes works
    if I write the fucntion from scratch, but the if I add const metrics, it breaks and even If I remove const metrics,
    it remains broken.
 */


const puppeteer = require('puppeteer');

 async function start(){
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://0.0.0.0:8000/sum.html');
    //test(page);
    console.log("*********************************");
    page.on('console', async e => { const args = await Promise.all(e.args().map(a => a.jsonValue()));console[e.type() === 'warning' ? 'warn' : e.type()](...args); });
    
    for(let i = 0; i < 30000; i++){ 
       if(i%10000==0){
          console.log("Halfway There!");}}
    
    await browser.close();
 }
 
 async function test( page){
    console.log("test called")
    page.on('console', async e => { const args = await Promise.all(e.args().map(a => a.jsonValue()));console[e.type() === 'warning' ? 'warn' : e.type()](...args); });
 }

 start();