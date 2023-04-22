

<script>
    import { page } from '$app/stores';
    import { onMount } from 'svelte';

    //get url params
    const url = $page.url;  //url
    const season = url.searchParams.get('season') //parse out the season



    /*
    let cards = [];
    //getting data from db
    async function fetchPerformances() {
      console.log('GETTING THE PERFORAMRNECSECS');
      const response = await fetch('http://127.0.0.1:5000/get_season_performances',
        method: 'POST', headers: {
          Accept: 'application/json', Content-Type: 'application/json'},
        body: JSON.stringify({ title: season }));
      const data = await response.json();
      cards = data.performances;
    }
    fetchPerformances();
    */


    //OLD HARD CODED DATA

    /*
    const cards = [
      { id: 1, title: "Card 1", content: "This is the content for Card 1" },
      { id: 2, title: "Card 2", content: "This is the content for Card 2" },
      { id: 3, title: "Card 3", content: "This is the content for Card 3" }
    ];
     */

    //NEW GETTING DATA FROM DATABSE
    let cards = [];
    async function fetch_performances() {
		let response = await fetch('http://127.0.0.1:5000/get_season_performances', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ title: season })
		});

		const out = await response.json();
		cards = out.performances;
	}
    fetch_performances();
    //END GETTING DATA FROM DB


    //list of cards selected
    let selectedCards = [];

    //handle when a card is selected
    const toggleSelection = (card) => {
      if (selectedCards.includes(card)) {
        selectedCards = selectedCards.filter((c) => c !== card);
      } else {
        selectedCards = [...selectedCards, card];
      }
    };



    //handles confirm button
    function confirm_selection(){
      //check for nothing selected
      if(selectedCards.length <= 0){
        alert("ERROR: you have not selected anything");
      } else {
        //create the string to send with the selections
        //it will be the id's seperated by dashes
        let combined = selectedCards.map(item => item.id).join('-'); //the combineds id's spererated by dashes as one string
        alert(`Your selection is ${combined}`)


        //TODO - continue HERE. Take the 'combined' string of id's and send it to a new page
        //will have to make that new page and make it so that page processes the payment information
      }
    }

    //check user is logged in
    let email = '';
    onMount(async () => {
		email = sessionStorage.getItem('user');
		if (email === null) {
          alert('You need to be logged in first, please log in');
          window.location.href = '/seasonpass/selectseason';
        }
	});

</script>



<style>
  .card {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    cursor: pointer;
  }

  .selected {
    background-color: #e6f7ff;
    border: 1px solid #1890ff;
  }
</style>





<h1>You selected the season, {season}. Now select the performances you would like to attend. Only select ONE per production.</h1>

<div>
  {#each cards as card}
    <div
      class="card {selectedCards.includes(card) ? 'selected' : ''}"
      on:click={() => toggleSelection(card)}
    >
      <h3>{card.title}</h3>
      <p>{card.content}</p>
    </div>
  {/each}
</div>

<div>
  <button on:click={confirm_selection}>Click here to confirm your selection</button>
</div>