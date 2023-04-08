<!-- 
    Ticket Dropdown Component
    This component is  on the page to buy tickets for a 
    specific event and is used to create the Select where
    users can select how many tickets they want to buy.

    **
      This is an unused component for now but might be used
      later. Will get rid of it if it's decided it's not
      needed.
    **
-->

<script>
    import { Select } from "flowbite-svelte"

    /**
	 * @type {any}
	 */
    let selected
    const array = [
        { value: 1, name: "1 ticket" },
		{ value: 2, name: "2 tickets" },
		{ value: 3, name: "3 tickets" },
        { value: 4, name: "4 tickets" },
		{ value: 5, name: "5 tickets" },
		{ value: 6, name: "6 tickets" },
        { value: 7, name: "7 tickets" },
		{ value: 8, name: "8 tickets" },
    ]
</script>

<!-- Display Select with options of number of tickets 1-8 -->
<Select items={array} size="lg" bind:value={selected} placeholder=""/>