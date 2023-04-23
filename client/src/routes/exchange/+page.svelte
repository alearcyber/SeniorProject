<script>
    import {onMount} from "svelte";
    import { page } from '$app/stores';

    //get url params
    const url = $page.url;  //url




    //user clicks the button to indicate they want to exchange tickets
    function confirm_selection(){
      //check that it is not empty
      if(selected_seats.length === 0){
        alert('You did not select any tickets to exchange. Going back...');
      } else {
        alert('The selected tickets will be exchanged and cost reduced from your next purchase!');
        console.log("Selected Tickets:", selected_seats);

        //add a list of the ticket ids and costs to sessionStorage
        //will be formatted like so:
        //  id1,cost1;id2,cost2
        //This is so it can be parsed easily later on
        let out = '';
        for(let i = 0; i < selected_seats.length; i++){
          let s = selected_seats[i];
          out = out.concat(s.id,',',s.price,';');
        }
        out = out.slice(0, -1); //remove last semicolon
        sessionStorage.setItem('exchange',out);
      }
      window.location.href = '/tickets';
    }



    let email;

    //on mount function
    onMount(async () => {

      //get users email, reject them if they are not logged in
      email = sessionStorage.getItem('user');
      if (email === null) {
        alert('You need to be logged in first, please log in');
        window.location.href = '/tickets';
      }

      //remove any exchange info from session storage
      sessionStorage.removeItem('exchange');

      //grab the user's
      get_owned_seats();
	});





    let seats = []
    let selected_seats = [];




    //retreive seats owned by the person that are eligeble for exchanging
    async function get_owned_seats(){
      let response = await fetch('http://127.0.0.1:5000/get_my_tickets', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({'email': email})
		});
		const out = await response.json();
		seats = out.seats;
    }



    //keeps track of chosen tickets
    const toggleSelection = (card) => {
      if (selected_seats.includes(card)) {
        selected_seats = selected_seats.filter((c) => c !== card);
      } else {
        selected_seats = [...selected_seats, card];
      }
    };

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

  h1 {
    font-size: 50px;
  }

  button {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    color: #fff;
    background-color: #4caf50;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #3e8e41;
  }
</style>

<h1>Select Your Tickets To Exchange</h1>
<div>
  {#each seats as seat}
    <div
      class="card {selected_seats.includes(seat) ? 'selected' : ''}"
      on:click={() => toggleSelection(seat)}
    >
      <h3>{seat.title}  |  {seat.date}  |  {seat.time}</h3>
      <p> Seat {seat.row}{seat.num} in the {seat.sec}</p>
    </div>
  {/each}
</div>

<div>
  <button on:click={confirm_selection}>Click Here Exchange Tickets</button>
</div>