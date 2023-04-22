/* Seat Store
 * This store is an array that stores all of the 
 * selected seats on the seat graphics.
 */

import { derived, writable } from "svelte/store"

export const SeatStore = writable([])

//add a seat to the store
export const addSeat = (seat) => {
    SeatStore.update((currentSeats) => [...currentSeats, seat])
}

//remove a seat from the store
export const removeSeat = (seat) => {
    SeatStore.update((currentSeats) => currentSeats.filter((s) => s.id !== seat.id))
}

//clear the store
export const clear = () => {
    SeatStore.update(() => [])
}

export const sum = derived(
	SeatStore,
	$SeatStore => $SeatStore.reduce((total, item) => total + item.price, 0)
);