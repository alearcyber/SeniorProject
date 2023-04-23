<script>
  import {onMount} from "svelte";
  import {Input, Label, Button, Select, Heading, P, Hr, Checkbox} from 'flowbite-svelte';
  import Center from '../../../layouts/center.svelte'; //import Center layout
  import {page} from '$app/stores';


  let email = '';
  const url = $page.url; //get url
  let performance_id = url.searchParams.get('pid'); //parse out url parameters, the performance id specifically
  let section = url.searchParams.get('sec');
  let row = url.searchParams.get('row');
  let number = url.searchParams.get('num');
  let season = url.searchParams.get('season');
  let name = '';
  let address = '';


    //when user presses button, do stuff
    const button_alert = async () => {

      //send info to database
      const response = await fetch('http://localhost:5000/buy_season_ticket', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          number,
          row,
          section,
          season,
          email,
          name,
          address,
        })
      });

      alert('your season ticket has been purchased! Good For you.');
      window.location.href = '/';
    }


    onMount(async () => {
      email = sessionStorage.getItem('user');
    });
</script>



<Center>
  <div class="grid grid-cols-2 gap-10">
    <div>
      <Heading tag="h2" customSize="text-4xl font-extrabold">Payment</Heading>
      <P class="my-4 text-gray-500 text-center">Enter your information.</P>
      <form>
          <div class="mb-6">
            <Label for="name" class="mb-2">Your Name:</Label>
            <Input bind:value={name} type="text" id="name" placeholder="John Doe" required />
          </div>

          <div class="mb-6">
            <Label for="email" class="mb-2">Email address</Label>
            <Input bind:value={email} type="email" id="email" placeholder="john.doe@company.com" required />
          </div>
          <div class="mb-6">
            <Label for="address1" class="mb-2">Address</Label>
            <Input bind:value={address} type="text" id="address1" placeholder="Street, etc." required />
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
        <Button type="submit" on:click={button_alert}>Submit</Button>
      </form>
    </div>
      <div>
          <Heading tag="h2" customSize="text-4xl font-extrabold">Reservation Info</Heading>
          <p>Price: 75$   |   Season: {season}</p>
          <p>Seat {row}{number} in the {section}</p>
          <p></p>
      </div>



</Center>