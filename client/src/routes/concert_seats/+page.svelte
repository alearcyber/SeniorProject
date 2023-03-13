<!-- 
    Concert Hall Seats Page
    This page is where the customer will select a seat for an 
    event in the Civic Center Concert Hall.
-->

<script>
    import ConcertHall from "../../components/ConcertHall.svelte"
    import { Listgroup, ListgroupItem, Button, Dropdown, DropdownItem, DropdownDivider, Chevron } from 'flowbite-svelte'
	// @ts-ignore
	import TicketCard from "../../components/TicketCard.svelte"

    /**
	 * @type {{ seats: any; }}
	 */
     export let data
</script>

<div class="block p-6 bg-blue-700 border border-gray-700 shadow-md dark:bg-gray-800 dark:border-gray-700 text-white text-xl font-serif max-w-50rem">
    <h1 class="text-2xl font-bold">Phantom of the Opera</h1>
    <h2>Civic Center Playhouse</h2>
    <h1 class="">May 09 2023</h1>
    <h2 class="">7:00 PM</h2>
</div>
<div class="flex content-center">
    <div class="inline-block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
        <ConcertHall seats={data.seats} />
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
        <Listgroup class="mt-6">
            <h1 class="text-center bg-white text-black font-bold rounded-t-lg text-2xl">
                Available Seats
            </h1>
            <ListgroupItem class="text-base font-semibold gap-2">
                <TicketCard />
            </ListgroupItem>
        </Listgroup>
    </div>
</div>