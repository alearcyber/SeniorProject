<!-- 
    Seat Indicator Component 
    This component is the seat indicator with the ability to indicate 
    whether it is available, selected, or occupied. 
-->

<script>
    import { Indicator } from "flowbite-svelte"
    import { Check } from "svelte-heros-v2" //import checkmark graphic
    
    export const states = {
        available: 'available',
        occupied: 'occupied', 
        selected: 'selected'
    }

    export let initialSeatState = states.available

    let seatState = initialSeatState

    //Change seat from available to selected and vice versa when clicked
    function handleSeatClick() {
        if (seatState === states.available) {
            seatState = states.selected
        } else if (seatState === states.selected) {
            seatState = states.available
        }
    }
</script>

<span on:click={handleSeatClick} on:keypress={handleSeatClick} class="flex items-center">
    {#if seatState === states.available} <!-- Seat is blue if available -->
        <Indicator color="blue"/>
    {:else if seatState === states.selected} <!-- Seat is green if selected -->
        <Indicator class="bg-green-400">
            <Check color="white" size="10"/>
        </Indicator>
    {:else} <!-- Seat is gray if occupied -->
        <Indicator color="gray"/>
    {/if}
</span>