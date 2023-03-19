<!-- 
    Playhouse Seats Page
    This page is where the customer will select a seat for an 
    event in the Civic Center Playhouse.
-->

<script>
// @ts-nocheck

    import Playhouse from "../../components/Playhouse.svelte"
    import { Listgroup, ListgroupItem, Button, Dropdown, DropdownItem, DropdownDivider, Chevron } from 'flowbite-svelte'
	// @ts-ignore
	import TicketCard from "../../components/TicketCard.svelte"

    /**
	* @type {{ seats: {}; tickets: Array<{}>; performance: {title: string;}; }}
	*/
    export let data
    /**
	* @type {any[]}
	*/
    let seats = [];
    let tickets = Object.assign(...data.tickets.map(ticket => ({ [ticket.seat_id]: ticket })))

    Object.keys(data.seats).forEach(section => seats.push(...data.seats[section]))
</script>

<div class="block p-6 bg-blue-700 border border-gray-700 shadow-md dark:bg-gray-800 dark:border-gray-700 text-white text-xl font-serif max-w-50rem">
    <h1 class="text-2xl font-bold">{data.performance.title}</h1>
    <h2>{data.performance.venue}</h2>
    <h1 class="">{data.performance.date}</h1>
    <h2 class="">{data.performance.time}</h2>
</div>
<div class="flex content-center">
    <div class="inline-block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
        <Playhouse seats={data.seats} tickets={tickets} />
    </div>

    <div class="inline-block p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 max-w-50rem">
          <Button><Chevron>2 tickets</Chevron></Button>
          <Dropdown>
            <DropdownItem>1 ticket</DropdownItem>
            <DropdownDivider/>
            <DropdownItem>2 tickets</DropdownItem>
            <DropdownDivider/>
            <DropdownItem>3 tickets</DropdownItem>
          </Dropdown>
        <Listgroup class="mt-6 max-h-screen overflow-auto">
            <h1 class="text-center bg-white text-black font-bold rounded-t-lg text-2xl">
                Available Seats
            </h1>
            {#each seats as { id, sec, row, seat } }
                <!-- {#if ![undefined, null].includes(tickets[id]?.user_id) } -->
                    <ListgroupItem class="text-base font-semibold gap-2">
                        <TicketCard section={sec} row={row} seat={seat} price={tickets[id]?.price ?? 0}/>
                    </ListgroupItem>
                <!-- {/if} -->
            {/each}
        </Listgroup>
    </div>
</div>

  
  