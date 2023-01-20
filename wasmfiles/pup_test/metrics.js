const puppeteer = require('puppeteer');
process.argv.forEach(async function (val, index, array) {
    if (index == 2)
    {
    const browser = await puppeteer.launch();
    const page =await browser.newPage();const metrics = await page.metrics();
    console.log(metrics);
    await page.goto("http://0.0.0.0:8000/"+val);
    await browser.close();
    }
  });