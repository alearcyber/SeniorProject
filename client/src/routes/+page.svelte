<script>
    import { CarouselTransition } from "flowbite-svelte"
    import Center from '../layouts/center.svelte'
    import { images } from '../carousel_data/+server.js'

    let showThumbs=false
    let showCaptions=false
</script>

<Center>
    <div class="scale-125 pt-10">
        <CarouselTransition {images} {showCaptions} {showThumbs} />
    </div>
</Center>