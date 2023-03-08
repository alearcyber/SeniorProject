<!-- 
    Seat Component 
    This component is the seat with the ability to indicate 
    whether it is available, selected, or occupied. 
-->

<script>
    /**
	 * @type {{ id: any; x: any; y: any; r: any; status: any; }}
	 */
     export let seat

     export const states = {
        available: 'available',
        occupied: 'occupied', 
        selected: 'selected'
    }

    let newSeat = seat

    if (newSeat?.status === undefined) {
        newSeat.status = 'available'
    }

     //Change seat from available to selected and vice versa when clicked
     function handleSeatClick() {
        if (newSeat.status === states.available) {
            newSeat.status = states.selected
        } else if (newSeat.status === states.selected) {
            newSeat.status = states.available
        }
    }
</script>

<g on:click={handleSeatClick} on:keypress={handleSeatClick}>
    {#if newSeat.status === states.available} <!-- Seat is blue if available -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat cursor-pointer"
            cx={seat.x}
            cy={seat.y}
            r={seat.r}
            fill="blue"
        />
    {:else if newSeat.status === states.selected} <!-- Seat is green if selected -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat cursor-pointer"
            cx={seat.x}
            cy={seat.y}
            r={seat.r}
            fill="limegreen"
        />
    {:else} <!-- Seat is gray if occupied -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat"
            cx={seat.x}
            cy={seat.y}
            r={seat.r}
            fill="gray"
        />
    {/if}
</g>
