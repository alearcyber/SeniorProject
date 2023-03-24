import { writable } from "svelte/store"

export const SeatStore = writable([])

export const addSeat = (seat) => {
    SeatStore.update((currentSeats) => [...currentSeats, seat])
}

export const removeSeat = (seat) => {
    SeatStore.update((currentSeats) => currentSeats.filter((s) => s !== seat))
}

export const clear = () => {
    SeatStore.update(() => [])
}