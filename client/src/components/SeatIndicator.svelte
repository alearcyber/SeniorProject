<script>
    import { Indicator } from "flowbite-svelte"
    import { Check } from "svelte-heros-v2"
    
    export const states = {
        available: 'available',
        occupied: 'occupied', 
        selected: 'selected'
    }

    export let initialSeatState = states.available

    let seatState = initialSeatState

    function handleSeatClick() {
        if (seatState === states.available) {
            seatState = states.selected
        } else if (seatState === states.selected) {
            seatState = states.available
        }
    }
</script>

<span on:click={handleSeatClick} on:keypress={handleSeatClick} class="flex items-center">
    {#if seatState === states.available}
        <Indicator color="blue"/>
    {:else if seatState === states.selected}
        <Indicator class="bg-green-400">
            <Check color="white" size="10"/>
        </Indicator>
    {:else}
        <Indicator color="gray"/>
    {/if}
  </span>