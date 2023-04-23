<script>
    import Playhouse from "../../../components/Playhouse.svelte"
    import { Listgroup, ListgroupItem, Button } from 'flowbite-svelte'
	import TicketCard from "../../../components/TicketCard.svelte"
    import { SeatStore } from '../../../stores/SeatStore.js'
    import Legend from "../../../components/Legend.svelte"
    import { page } from '$app/stores';
    import { onMount } from 'svelte';


    //get url params
    const url = $page.url;  //url
    const season = url.searchParams.get('season'); //parse out the season
    const performances = url.searchParams.get('performances');


    //other stuff
    /**
	* @type {{ seats: {}; tickets: Array<{}>; performance: {title: string;}; }}
	*/
    export let data;
    data = data.data ?? data

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
    $: mySeatStore = $SeatStore //subscribe to seat store


    //go to the next page
    function next(){
        let s = mySeatStore[0];
        window.location.href = `/seasonpass/buyit?sec=${s.sec}&row=${s.row}&num=${s.seat}&season=${season}`;
    }

</script>


<!-- Performance information heading -->
<div class="block p-6 bg-blue-700 border border-gray-700 shadow-md dark:bg-gray-800 dark:border-gray-700 text-white text-xl font-serif max-w-50rem">
    <h1 class="text-2xl font-bold">Season: {season}</h1>
    <h2>{data.performance.venue}</h2>
    <h2>Please choose only 1 seat</h2>
</div>

<div class="min-w-max flex content-center">
    <!-- Seat graphic and legend -->
    <div {seats} class="grow inline-block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
        <Legend />
        <Playhouse bind:seats={data.seats} tickets={tickets} />
    </div>

    <!-- List of seats -->
    <div class="w-96 inline-block p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700 max-w-50rem">
        <!-- Display list of selected seats -->
        <Listgroup class="mt-6 max-h-screen overflow-auto">
            <h1 class="text-center bg-white text-black font-bold rounded-t-lg text-2xl">
                Your Seating Choice
            </h1>
            {#each mySeatStore.slice(0,1) as { id, sec, row, seat } }
                {#if seat }
                    <ListgroupItem class="text-base font-semibold gap-2">
                        <TicketCard section={sec} row={row} seat={seat} price=75$ />
                    </ListgroupItem>
                {/if}
            {/each}
        </Listgroup>
        <div>
            <Button on:click={next} class="w-full h-full" size="sm">Confirm Selection</Button>
        </div>
    </div>
</div>