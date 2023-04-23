<script>
    import {onMount} from "svelte";


    //check that the user is logged in
    let email = 'tom.bombadillo@arnornet.me';
    onMount(async () => {
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
            body: JSON.stringify({'email': email})
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


    function dummy() {
      console.log(cards);
    }



    //logical storage of the season passes in memory
    let season_pass_info = [
      {'id':1, 'email': 'ojhn@gmail.com', 'name': 'johntravolta', 'address': 'the road'},
      {'id':2, 'email': 'one', 'name': 'two', 'address': 'three'},
      {'id':3, 'email': 'asdfasdf', 'name': 'asdfasdf', 'address': 'twerf'},
    ]



    //this function populates the season apss info when the page loads
    async function populate_season_pass_info(){
      let response = await fetch('http://127.0.0.1:5000/get_season_pass_info', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'email': email})
        });
        const out = await response.json();
        season_pass_info = out.season_passes;
    }


    //this function updates the information for the database
    function handle_submit(event){
      event.preventDefault(); // prevent the default form submission behavior

      // get the form input values from the event.target object
      const formData = new FormData(event.target);
      const name = formData.get('name');
      const email = formData.get('email');
      const address = formData.get('address');
      const id = formData.get('id');

      // call your function with the form data as arguments
      alert(`the name is ${email}, ${name}, ${address}, ${id}`);
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


<h1>Past Season Pass Info</h1>


<div>
    {#each season_pass_info as card}
        <div
                class="card {selectedCards.includes(card) ? 'selected' : ''}"
                on:click={() => toggleSelection(card)}
        >
            <p>Season Pass</p>
            <form on:submit|preventDefault={handle_submit}>

                <input name="id" type="text" value={card.id} hidden>

                <label>
                    Email:
                    <input name="email" type="text" value={card.email}>
                </label>

                <label>
                    Name:
                    <input name="name" type="text" value={card.name}>
                </label>

                <label>
                    Address:
                    <input name="address" type="text" value={card.address}>
                </label>
                <button type="submit">Submit</button>
            </form>
        </div>
    {/each}
</div>

<div>
    <button on:click={dummy}>Click here to confirm your selection</button>
</div>