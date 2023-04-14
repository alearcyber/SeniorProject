<!-- 
    Seat Component 
    This component is the seat with the ability to indicate 
    whether it is available, selected, or occupied. 
-->

<script>
// @ts-nocheck

    import { SeatStore, addSeat, removeSeat } from '../stores/SeatStore.js'

    /**
	* @type {{ id: any; x: any; y: any; r: any; status: any; }}
	*/
    export let seat
    /**
	* @type {[{ seat_id: any; user_id: any; performance_id: any; price: any }]}
	*/
    // @ts-ignore
    export let ticket = {}
    // @ts-ignore
    const ticketSale = ![null].includes(ticket?.user_id)

    export const states = {
        available: 'available',
        occupied: 'occupied', 
        selected: 'selected'
    }

    seat.status = ticketSale ? 'occupied' : 'available'

    let mySeatStore
    $: mySeatStore = $SeatStore //subscribe to seat store

    //Change seat from available to selected and vice versa when clicked
    function handleSeatClick() {
        if (seat.status === states.available) {
            seat.status = states.selected
            addSeat({...seat, price: ticket.price}) //add seat to seat store
        } else if (seat.status === states.selected) {
            seat.status = states.available
            removeSeat(seat) //remove seat from seat store
        }
    }
</script>

<g on:click={handleSeatClick} on:keypress={handleSeatClick}>
    {#if seat.status === states.available} <!-- Seat is blue if available -->
        <circle 
            data-component="svg_seat" 
            id={seat.id}
            class="seat cursor-pointer"
            cx={seat.x}
            cy={seat.y}
            r={seat.r}
            fill="blue"
        />
    {:else if seat.status === states.selected} <!-- Seat is green if selected -->
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
