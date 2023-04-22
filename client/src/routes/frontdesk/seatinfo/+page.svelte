<script>
    import {onMount} from "svelte";
    import Radio from './Radio.svelte'
    import { page } from '$app/stores';





    //get url params
    const url = $page.url;  //url
    const number = url.searchParams.get('number')
    const row = url.searchParams.get('row')
    const section = url.searchParams.get('section')
    const performance_id = url.searchParams.get('id')
    const performance_title = url.searchParams.get('title')




    //section map
    //maps the section to what word should be displayed
    var section_name_map = {"main_orch": "Main Orchestra",
      "left_orch": "Left Orchestra",
      "right_orch": "Right Orchestra",
      "balc": "Balcony",
      "right_box": "Right Box",
      "left_box": "Left Box",
      "left_loge": "Left Loge",
      "right_loge": "Right Loge"}



    //handles going back to the previous page
    function go_back(){
        window.location.href = `/frontdesk/manager?title=${performance_title}&id=${performance_id}`;
    }


    //seat info
    //status can ONLY be 'paid', 'reserved', or 'available'
    let seat = { status: '', price: 0, email: ''};
    let paymentMethod = 'cash';


    //radio button options. must be either 'card', 'cash', or 'check' as value to send back to database
    const options = [{
		value: 'cash',
		label: 'Cash',
	}, {
		value: 'card',
		label: 'Credit Card',
	}, {
		value: 'check',
		label: 'Check',
	}]



    //sends the payment stuff back to the database
    async function send_payment_to_db() {
		let response = await fetch('http://127.0.0.1:5000/handle_frontdesk_payment', {
			method: 'POST',
			headers: {Accept: 'application/json', 'Content-Type': 'application/json'},
			body: JSON.stringify({ 'performance_id':performance_id, 'number':number, 'row':row, 'section':section, 'payment_method': paymentMethod})
		});
		const out = await response.json();
		return out.status;
	}







    //info needed to send back to database -> (performance_id, number, row, section, payment_method)
    //handle changes made when a payment method is selected
    async function handleSubmit(){
        //check that the seat is NOT already paid, reject attempt to submit payment
        if(seat.status === 'paid'){
          alert("The seat has already been payed for.");
        } else{
          //TODO - handle payment for available seat...
          let did_it_work = await send_payment_to_db();
          alert(`Processing Payment....\nPayment Successfully Received!\nDid it work:${did_it_work}`);
        }
    }

    //get info on the seat when the page is first loaded from db
    async function get_seat_info() {
		let response = await fetch('http://127.0.0.1:5000/frontdesk_seat_info', {
			method: 'POST',
			headers: {Accept: 'application/json', 'Content-Type': 'application/json'},
			body: JSON.stringify({ 'performance_id':performance_id, 'number':number, 'row':row, 'section':section})
		});
		const out = await response.json();
		seat = out.seat_info;
	}



    //onMount function
    onMount(async () => {
        //get seat data
		get_seat_info();
	});

</script>


<style>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 20vh;
  }

  .seat-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
    padding: 1rem;
    background-color: #f5f5f5;
    border-radius: 0.5rem;
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





<div class="container">
  <h1>Seat Information</h1>
  <div class="seat-info">
    <p>Number: {number}  |  Row: {row}  |  Section: {section_name_map[section]}</p>
    <p>Email of Patron: {seat.email}</p>
    <p>Status: {seat.status}</p>
    <p>Price: {seat.price}</p>
  </div>
  <Radio {options} fontSize={16} legend='Choose A Payment Method' bind:userSelected={paymentMethod}/>

</div>

<div>
  <button on:click={handleSubmit}>Confirm Changes</button>
  <button on:click={go_back}>Go Back</button>
</div>

