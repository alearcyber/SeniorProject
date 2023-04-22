<!--
    Payment Page
    This page is where the customer will pay for their ticket(s)
-->

<script>
  import {onMount} from "svelte";
  import { Input, Label, Button, Select, Heading, P, Hr, Checkbox } from 'flowbite-svelte'
  import Radio from './Radio.svelte'
  import Center from '../../layouts/center.svelte' //import Center layout
  import Checkout from '../../components/Checkout.svelte'
  import { SeatStore } from '../../stores/SeatStore.js'
  import { page } from '$app/stores'

  const url = $page.url; //get url
  let performance_id = url.searchParams.get('pid') //parse out url parameters, the performance id specifically

  /**
  * @type {any[]}
  */
  let mySeatStore
  $: mySeatStore = $SeatStore //subscribe to seat store

  let email = ''
  let payment_method = 'card'


  //onMount function
  onMount(async () => {
    //grab the users email
    if (!(sessionStorage.getItem('user') === null)){
      email = sessionStorage.getItem('user');
    }
  });


  const button_alert = async () => {
    //grab number, row, and section or each selected seat
    let seat_data = [];
    for(let i = 0; i < mySeatStore.length; i++){
      //[number, row, section]
      let s = mySeatStore[i];
      seat_data.push([s.seat, s.row, s.sec]);
    }


    const response = await fetch('http://localhost:5000/purchase_tickets', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        //seats_ids: mySeatStore.map(seat => seat.id),
        seat_data: seat_data,
        email,
        performance_id,
        'payment_method': paymentMethod,
      })
    })

    console.log({ response })

    if(paymentMethod === 'card'){
      alert('Thank you for your purchase! Your order has been confirmed.')
    } else {
      alert('Thank you! Your seats have been reserved.')
    }
  };


  //radio button options. must be either 'card', 'cash', or 'check' as value to send back to database
  let paymentMethod = 'card';
  const options = [{
    value: 'cash',
    label: 'Cash',
  }, {
    value: 'card',
    label: 'Credit Card',
  }, {
    value: 'check',
    label: 'Check',
  }];

</script>

<Center>
  <div class="grid grid-cols-2 gap-10">
    <div>
      <Heading tag="h2" customSize="text-4xl font-extrabold">Payment</Heading>
      <P class="my-4 text-gray-500 text-center">Enter your information.</P>
      <form>
        <div class="grid gap-6 mb-6 md:grid-cols-2">
          <div>
            <Label for="first_name" class="mb-2">First name</Label>
            <Input type="text" id="first_name" placeholder="John" required  />
          </div>
          <div>
            <Label for="last_name" class="mb-2">Last name</Label>
            <Input type="text" id="last_name" placeholder="Doe" required />
          </div>
        </div>
          <div class="mb-6">
            <Label for="email" class="mb-2">Email address</Label>
            <Input bind:value={email} type="email" id="email" placeholder="john.doe@company.com" required />
          </div>
          <div class="mb-6">
            <Label for="address1" class="mb-2">Address 1</Label>
            <Input type="text" id="address1" placeholder="Street, etc." required />
          </div>
          <div class="mb-6">
            <Label for="address2" class="mb-2">Address 2</Label>
            <Input type="text" id="address2" placeholder="Apt #, etc." />
          </div>
        <div class="grid gap-6 mb-6 md:grid-cols-2">
          <div>
            <Label for="city" class="mb-2">City</Label>
            <Input type="text" id="city" placeholder="Huntsville" required />
          </div>
          <div>
            <Label for="state" class="mb-2">State</Label>
            <Input type="text" id="state" placeholder="Alabama" required />
          </div>
          <div>
            <Label for="zipcode" class="mb-2">Zipcode</Label>
            <Input type="text" id="zipcode" placeholder="" required />
          </div>
          <div>
            <Label for="country" class="mb-2">Country</Label>
            <Input type="text" id="country" placeholder="United States" required />
          </div>
        </div>
        {#if paymentMethod === 'card'}
          <div class="mb-6">
            <Label for="card_number" class="mb-2">Card Number</Label>
            <Input type="text" id="card_number" placeholder="**** **** **** ****" required />
          </div>
          <div class="grid gap-6 mb-6 md:grid-cols-2">
            <div>
              <Label for="date" class="mb-2">Expiration MM/YY</Label>
              <Input type="text" id="date" placeholder="01/01" required />
            </div>
            <div>
              <Label for="security_code" class="mb-2">Security Code</Label>
              <Input type="text" id="security_code" placeholder="***" required />
            </div>
          </div>
        {/if}
        <Radio {options} fontSize={16} legend='Choose A Payment Method' bind:userSelected={paymentMethod}/>
        {#if !(paymentMethod === 'card')}
          <p>Note: You must pay at the door if you pay with check or cash</p>
        {/if}
        <Button type="submit" on:click={button_alert} href="/">Submit</Button>
      </form>
    </div>
    <Checkout />
</Center>
