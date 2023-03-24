<!-- 
    Concert Hall Seats Page
    This page is where the customer will select a seat for an 
    event in the Civic Center Concert Hall.
-->

<script>
    import ConcertHall from "../../components/ConcertHall.svelte"
    import { Listgroup, ListgroupItem, Button } from 'flowbite-svelte'
	import TicketCard from "../../components/TicketCard.svelte"
    import { SeatStore } from '../../stores/SeatStore.js'
    import Legend from "../../components/Legend.svelte"

    /**
	* @type {{ seats: {}; tickets: Array<{}>; performance: {title: string;}; }}
	*/
    export let data
    /**
	* @type {any[]}
	*/
    let seats = [];
    let dataSeats = data.seats
    let tickets = Object.assign(...data.tickets.map(ticket => ({ [ticket.seat_id]: ticket })))

    Object.keys(dataSeats).forEach(section => seats.push(
        ...dataSeats[section].map(seat => ({ ...seat, ...tickets[seat.id] }))
    ))

    let mySeatStore
    $: mySeatStore = $SeatStore
</script>

<!-- Performance information heading -->
<div class="block p-6 bg-blue-700 border border-gray-700 shadow-md dark:bg-gray-800 dark:border-gray-700 text-white text-xl font-serif max-w-50rem">
    <h1 class="text-2xl font-bold">{data.performance.title}</h1>
    <h2>{data.performance.venue}</h2>
    <h1 class="">{data.performance.date}</h1>
    <h2 class="">{data.performance.time}</h2>
</div>

<div class="flex content-center">
    <!-- Seat graphic -->
    <div {seats} class="inline-block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
        <Legend />
        <ConcertHall bind:seats={data.seats} tickets={tickets} />
    </div>

    <!-- List of seats -->
    <div class="w-96 inline-block p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 max-w-50rem">
        <!-- Display list of available seats -->
        <Listgroup class="mt-6 max-h-screen overflow-auto">
            <h1 class="text-center bg-white text-black font-bold rounded-t-lg text-2xl">
                Your Tickets
            </h1>
            
            {#each mySeatStore as { id, sec, row, seat } }
                {#if seat } 
                    <ListgroupItem class="text-base font-semibold gap-2">
                        <div class="relative">
                            <Button pill={true} class="!p-2 absolute right-0">
                                <img
                                    src="../x.svg"
                                    alt="Remove ticket"
                                    class="h-3 sm:h-3"
                                />
                            </Button>
                        </div>
                        <TicketCard section={sec} row={row} seat={seat} price={tickets[id]?.price ?? 0} />
                    </ListgroupItem>
                {/if}
            {/each}
        </Listgroup>
    </div>
</div>