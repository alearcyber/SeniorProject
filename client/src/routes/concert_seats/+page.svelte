<!-- 
    Concert Hall Seats Page
    This page is where the customer will select a seat for an 
    event in the Civic Center Concert Hall.
-->

<script>
    import ConcertHall from "../../components/ConcertHall.svelte";

    /**
	 * @type {{ seats: any; }}
	 */
     export let data
</script>

<ConcertHall seats={data.seats}/>