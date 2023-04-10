
// @ts-ignore
export async function load({ fetch }) {
   try {
       const response = await fetch('http://127.0.0.1:5000/upcomingperformances') //call the api
       const json = await response.json() // wait for response and parse the json
       return json; // return the json

   } catch (error) {
       console.log("AN ERROR HAPPENED:", error)
   }
}