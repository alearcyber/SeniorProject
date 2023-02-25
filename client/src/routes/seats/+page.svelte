<!-- 
    Seats Page
    This page is where the customer will select a seat for a specific event.
-->

<script>
    import { Img } from "flowbite-svelte"
    import SeatIndicator from "../../components/SeatIndicator.svelte" //import seatindicator component
</script>

<div>
    <!-- format stadium graphic -->
    <div
        class="block relative max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700"
        style="min-height: 788px"
    >
        <!-- link to stadium image -->
        <Img
            size="max-w-full"
            alt="Civic Center Playhouse"
            src="https://mapsapi.tmol.io/maps/geometry/image/7/99/79985?removeFilters=ISM_Shadow&amp;avertaFonts=true&amp;app=CCP"
            class="absolute block"
        />

        <!-- format seat indicators onto image -->
        <div class="absolute w-max-full">
            <SeatIndicator />
        </div>
    </div>
</div>