<script>
    import { Img } from "flowbite-svelte"
	import SeatIndicator from "../../components/SeatIndicator.svelte"
</script>
  <div>
    <div
     class="block relative max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700"
     style="min-height: 788px"
    >
        <Img
            size="max-w-full"
            alt="Civic Center Playhouse"
            src="https://mapsapi.tmol.io/maps/geometry/image/7/99/79985?removeFilters=ISM_Shadow&amp;avertaFonts=true&amp;app=CCP"
            class="absolute block"
        />
        <div class="absolute w-max-full">
            <SeatIndicator />
        </div>
    </div>
  </div>