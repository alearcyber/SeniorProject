<!-- 
    Playhouse Seats Page
    This page is where the customer will select a seat for an 
    event in the Civic Center Playhouse.
-->

<script>
    import Playhouse from "../../components/Playhouse.svelte";

    /**
	 * @type {{ seats: any; }}
	 */
     export let data
</script>

<Playhouse seats={data.seats} />