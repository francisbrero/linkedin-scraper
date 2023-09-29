var query = process.argv[2];
var url = 'https://www.linkedin.com/feed/'
var login_url = 'https://www.linkedin.com/login'
const browserObject = require('./browser');

require('dotenv').config();
var username = process.env.LINKEDIN_USERNAME;
var password = process.env.LINKEDIN_PASSWORD;

var main = (async () => {  
    let browserInstance = browserObject.startBrowser();
    let browser;
    try{
        browser = await browserInstance;
    
        let page = await browser.newPage();
        // set the viewport so we know the dimensions of the screen
        await page.setViewport({ width: 1280, height: 800 })
        // Log into Linkedin using the credentials in the .env file
        await page.goto(login_url);
        // wait for 3 seconds to make sure the page loads
        await new Promise(r => setTimeout(r, 3000));
        await page.type('#username', username);
        await page.type('#password', password);
        // press enter after typing in the password to submit the form
        await new Promise(r => setTimeout(r, 1000));
        // click the sign in button based on class name
        await page.click('.btn__primary--large');
        await new Promise(r => setTimeout(r, 1000));
        
        // go to the page we want to scrape
        await page.goto(url);
        // wait for 3 seconds to make sure the page loads
        await new Promise(r => setTimeout(r, 5000));
        // take a screenshot for debugging purposes
        await page.screenshot({ path: './debug/1_screen_load.png' });
        
        // enter the query into the search bar and hit enter
        await page.waitForSelector('#search-global-typeahead__input');
        await page.type('#search-global-typeahead__input', query);
        await page.keyboard.press('Enter');

        // wait for the page to load
        await new Promise(r => setTimeout(r, 5000));
        await page.waitForSelector('#ember321');
        // take a screenshot for debugging purposes
        await page.screenshot({ path: './debug/2_screen_search.png' });
    }
    catch(err){
        console.log(err);
    };

    // close the browser
    await browser.close();
    console.log('I am done')
 });

main()
  .catch((e) => console.log('err: ' + e));