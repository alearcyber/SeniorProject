<!-- 
    Front Desk Page
    This page is where the volunteers go to manage front desk.
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList, Listgroup, ListgroupItem, Checkbox, P } from 'flowbite-svelte'
    import TicketCard from "../../../components/TicketCard.svelte"
	import Center from '../../../layouts/center.svelte' //import Center layout

    let venue_input = "";

    //hard coded event data that will eventually be received from database
    let list = [
    { name: "Phantom of the Opera", date: "May 3", time: "6:00 p.m.", venue: "Civic Center Playhouse"
    },
    { name: "Hamilton", date: "May 7", time: "6:00 p.m.", venue: "Civic Center Concert Hall"
    },
    { name: "Wicked", date: "May 8", time: "6:00 p.m.", venue: "Civic Center Playhouse"
    },
  ]

    
    // Go to seating chart
    function href(item) {
        return item.venue === 'Civic Center Concert Hall' 
        ? '/concert_seats' 
        : '/playhouse_seats'

    }

    // Get date and time 
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    function monthNameToNum(monthname) {
        let month = monthNames.indexOf(monthname);
        return month ? month + 1 : 0;
    }
    function leadingZero(minutes) {
        if(minutes.startsWith("0"))
            return minutes = minutes - 0;
        else
            return minutes;
    }
    const d = new Date();
    
    let date = d.getDate()
    let month = d.getMonth() + 1;
    let year = d.getFullYear();
    let hour = d.getHours();
    let minute = d.getMinutes();
    let second = d.getSeconds();
    
    let hourValue = 0;
    let dayValue = "";

    if (hour > 0 && hour <= 12) {
        hourValue= hour;
    } else if (hour > 12) {
        hourValue= (hour - 12);
    } else if (hour == 0) {
        hourValue= 12;
    }

    
    dayValue += (hour >= 12) ? "p.m." : "a.m.";  // get AM/PM  
    
    let show_tickets = false;
    // Existing Reservations
    // Hard coded data get from database based on guest's name
    let sec = 1;
    let row = 1;
    let seat = 2
    let price = 5;
    let performance = "Wicked";


    const button_alert = () => {
        alert('Order has been confirmed.');
    };

</script>
  
<div class="ml-10 mb-20" >
    <Heading tag="h1" class="mb-16 ml-10" customSize=" text-left text-4xl font-extrabold  md:text-5xl lg:text-6xl">Front Desk Management</Heading>   

    <!-- Purchase Tickets for Guests -->
    <h3 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Purchase Seats for Guests: </h3> 

    <!-- Venue Field -->
    <Label class="space-y-2">
        <span>Venue</span>
        <Input type="text" bind:value={venue_input} name="venue_name" style= "width: 500px" placeholder="Civic Center Playhouse" required />
    </Label>


   <!-- Show Upcoming Shows -->   
    {#if venue_input == "Civic Center Playhouse"}
    <Heading tag="h1" class="mb-4 mt-3 text-blue-500" customSize="text-3xl font-extrabold  md:text-3xl lg:text-3xl">Upcoming Shows</Heading>
        <Listgroup items={list} let:item class="border-0 dark:!bg-transparent">
            <!-- Civic Center PlayHouse Shows -->
            {#if item.venue == "Civic Center Playhouse" }

                <!-- Morning Shows -->
                {#if dayValue == "a.m." && item.time.split(':')[0] >= hourValue && leadingZero(item.time.split(" ")[0].split(":")[1]) >= minute 
                    || monthNameToNum(item.date.split(' ')[0]) > month ||  (monthNameToNum(item.date.split(' ')[0]) == month && item.date.split(' ').pop() >= date)}
                <div class="flex items-center space-x-4">

                    <!-- format date of event -->
                    <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
                    {item.date}
                    </div>
                
                    <!-- format name, venue, and time of event -->
                    <div class="flex-1 min-w-0">
                    <p class="text-xl font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.venue}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.time}
                    </p>
                    </div>
                    <!-- Button linking to Seats page -->
                    <Button class="w-fit" href={href(item)}>
                        Buy tickets
                    </Button>
                </div>

                <!-- Night Shows -->
                {:else if dayValue == "p.m." && item.time.split(' ')[1] == "p.m."  && item.time.split(':')[0] >= hourValue  && leadingZero(item.time.split(" ")[0].split(":")[1]) >= minute
                    || monthNameToNum(item.date.split(' ')[0]) > month ||  (monthNameToNum(item.date.split(' ')[0]) == month && item.date.split(' ').pop() >= date)}
                <h1> {item.time.split(':')[0]}</h1>
                <div class="flex items-center space-x-4">

                    <!-- format date of event -->
                    <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
                    {item.date}
                    </div>
                
                    <!-- format name, venue, and time of event -->
                    <div class="flex-1 min-w-0">
                    <p class="text-xl font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.venue}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.time}
                    </p>
                    </div>
                    <!-- Button linking to Seats page -->
                    <Button class="w-fit" href={href(item)}>
                        Buy tickets
                    </Button>
                </div>
                {/if}
            {/if}
        </Listgroup>
              
        
    <!-- Civic Center Concert Halls Shows -->
    {:else if venue_input == "Civic Center Concert Hall"}
        <Heading tag="h1" class="mb-4 mt-3 text-blue-500" customSize="text-3xl font-extrabold  md:text-3xl lg:text-3xl">Upcoming Shows</Heading>
        <Listgroup items={list} let:item class="border-0 dark:!bg-transparent">
            {#if item.venue == "Civic Center Concert Hall" }

                <!-- Morning Shows -->
                {#if dayValue == "a.m." && item.time.split(':')[0] >= hourValue && leadingZero(item.time.split(" ")[0].split(":")[1]) >= minute 
                || monthNameToNum(item.date.split(' ')[0]) > month ||  (monthNameToNum(item.date.split(' ')[0]) == month && item.date.split(' ').pop() >= date)}
                <div class="flex items-center space-x-4">

                    <!-- format date of event -->
                    <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
                    {item.date}
                    </div>
                
                    <!-- format name, venue, and time of event -->
                    <div class="flex-1 min-w-0">
                    <p class="text-xl font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.venue}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.time}
                    </p>
                    </div>
                    <!-- Button linking to Seats page -->
                    <Button class="w-fit" href={href(item)}>
                        Buy tickets
                    </Button>
                </div>

                <!-- Night Shows -->
                {:else if dayValue == "p.m." && item.time.split(' ')[1] == "p.m."  && item.time.split(':')[0] >= hourValue && leadingZero(item.time.split(" ")[0].split(":")[1]) >= minute
                    || monthNameToNum(item.date.split(' ')[0]) > month ||  (monthNameToNum(item.date.split(' ')[0]) == month && item.date.split(' ').pop() >= date)}
                <div class="flex items-center space-x-4">

                    <!-- format date of event -->
                    <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
                    {item.date}
                    </div>
                
                    <!-- format name, venue, and time of event -->
                    <div class="flex-1 min-w-0">
                    <p class="text-xl font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.venue}
                    </p>
                    <p class="text-base text-gray-500 truncate dark:text-gray-400">
                        {item.time}
                    </p>
                    </div>
                    <!-- Button linking to Seats page -->
                    <Button class="w-fit" href={href(item)}>
                        Buy tickets
                    </Button>
                </div>
                {/if}
            {/if}
        </Listgroup>
        {/if}   
</div>


 <!-- Pay Reservations for Guests -->
<div class="ml-10" >
    <form class=" ml-1flex flex-col space-y-2" style="width:500px" >
        
        <h3 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Payment for Existing Reservations: </h3>

        <!-- Guest Name Field -->
        <Label class="space-y-2">
          <span>Guest Name</span>
          <Input type="text" name="guest_name" placeholder="Michael Scott" required />
        </Label>

        <!-- Submit button -->
        <Button type="submit" on:click={() => (show_tickets = true)} class="w-full1">Submit</Button>
    </form>

    <!-- Form to pay for reservations -->
    {#if show_tickets == true}
    <Center>
    <div class="grid grid-cols-2 gap-10">
        <div>

        <!-- Show tickets reserverd -->
          <Heading tag="h2" customSize="text-4xl font-extrabold">Tickets</Heading>
          {#if seat } 
                <ListgroupItem class="text-base font-semibold gap-2">
                    <Heading customSize="text-2xl font-extrabold text-left" >Performance: {performance}</Heading>
                    <TicketCard section={sec} row={row} seat={seat} price={price} />
                </ListgroupItem>
          {/if}
        </div>

        <!-- Payment Information -->
        <div>
          <Heading tag="h2" customSize="text-4xl font-extrabold">Payment</Heading>
          <P class="my-4 text-gray-500 text-center">Enter information.</P>
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
            <div>
              <Checkbox class="mb-5">Paid with Cash</Checkbox>
            </div>
            <Button type="submit" on:click={button_alert} href="/">Submit</Button>
          </form>
        </div>
    </div>
    </Center>
    {/if}

    </div>

 



