<script>
    import {onMount} from "svelte";


    //check that the user is logged in
    let email = '';
    onMount(async () => {
		email = sessionStorage.getItem('user');
		if (email === null) {
          alert('You need to be logged in first, please log in');
          window.location.href = '/';
        }

		fetch_performances();
	});




    //grabbing data from database
    let cards = [];
    async function fetch_performances() {
		let response = await fetch('http://127.0.0.1:5000/frontdesk_upcoming_performances', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ 'email': email})
		});
		const out = await response.json();
		cards = out.performances;
	}

    //handle when a card is selected
    let selectedCards = []; //list of cards selected
    const toggleSelection = (card) => {
      if (selectedCards.includes(card)) {
        selectedCards = selectedCards.filter((c) => c !== card);
      } else {
        selectedCards = [...selectedCards, card];
      }
    };


	//handles confirm button
    function confirm_selection() {
      //check for nothing selected
      if (selectedCards.length <= 0) {
        alert("ERROR: you have not selected anything");
      } else if (selectedCards.length > 1) {
        alert("ERROR: you have to select ONLY ONE performance.");
      } else {

        alert(`You chose ${selectedCards[0].title}!`)
        window.location.href = `/frontdesk/manager?title=${selectedCards[0].title}&id=${selectedCards[0].id}`;
        //TODO - continue HERE. Take the 'combined' string of id's and send it to a new page
        //will have to make that new page and make it so that page processes the payment information
      }
    }


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





<h1>Upcoming Performances for your Organization</h1>


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