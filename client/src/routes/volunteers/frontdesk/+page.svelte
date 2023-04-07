<!-- 
    Volunteer Navigation Page
    This page is where the volunteers go to manage front desk.
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList } from 'flowbite-svelte'

</script>
  
<div class="mb-20" >
    <Heading tag="h1" class="mb-16 ml-10" customSize=" text-left text-4xl font-extrabold  md:text-5xl lg:text-6xl">Front Desk Management</Heading>   

    <!-- Purchase Tickets for Guests -->
    <h3 class="ml-10 text-3xl font-medium text-gray-900 dark:text-white p-0">Purchase Seats for Guests: </h3> 
    <a href="/tickets" class=" ml-10 text-2xl text-blue-700 hover:underline dark:text-blue-500">Performance Selection</a>
</div>

<div class="ml-10" >
    <form class=" ml-1flex flex-col space-y-2" style="width:500px" action='/'>
        
        <!-- Pay Reservations for Guests -->
        <h3 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Payment for Existing Reservations: </h3>

        <!-- Guest Name Field -->
        <Label class="space-y-2">
          <span>Guest Name</span>
          <Input type="text" name="guest_name" placeholder="Michael Scott" required />
        </Label>


        <!-- Continue button: Go to payment page with guests reserved tickets from database -->
        <Button href="/" type="submit" class="w-full1">Continue</Button>
    </form>
</div>
 



