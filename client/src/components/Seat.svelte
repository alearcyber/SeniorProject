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
     /**
	 * @type {[{ seat_id: any; user_id: any; performance_id: any; price: any }]}
	 */
      export let ticket = {}

     export const states = {
        available: 'available',
        occupied: 'occupied', 
        selected: 'selected'
    }

    let newSeat = seat

    const ticketSale = ticket?.user_id !== null

    newSeat.status = ticketSale ? 'occupied' : 'available'

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
            r="68.5"
            fill="blue"
        />
    {:else if newSeat.status === states.selected} <!-- Seat is green if selected -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat cursor-pointer"
            cx={seat.x}
            cy={seat.y}
            r="68.5"
            fill="limegreen"
        />
    {:else} <!-- Seat is gray if occupied -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat"
            cx={seat.x}
            cy={seat.y}
            r="68.5"
            fill="gray"
        />
    {/if}
</g>
