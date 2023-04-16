<!-- 
    Payment Page
    This page is where the customer will pay for their ticket(s)
-->

<script>
  import { Input, Label, Button, Select, Heading, P, Hr, Checkbox } from 'flowbite-svelte'
	import Center from '../../layouts/center.svelte' //import Center layout
  import Checkout from '../../components/Checkout.svelte'
  
  const button_alert = () => {
    alert('Thank you for your purchase! Your order has been confirmed.')
  };

  let visible = true;

  function toggleVisible() {
      visible = !visible
  }

</script>

<!-- GET RID OF THIS
-->
<Button class="w-full h-full" size="sm" href="/season_pass">Season Pass</Button> 

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
            <Input type="email" id="email" placeholder="john.doe@company.com" required />
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
        {#if visible}
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
        <Checkbox class="mb-4" on:change={toggleVisible}>I'm paying with cash or check</Checkbox>
        <Button type="submit" on:click={button_alert} href="/">Submit</Button>
      </form>
    </div>
    <Checkout />
</Center>
