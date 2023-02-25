<!-- 
    Home Page
    This is the homepage for the site. 
-->

<script>
    import { CarouselTransition } from "flowbite-svelte"
    import Center from '../layouts/center.svelte' //import center layout
    import { images } from '../carousel_data/+server.js' //import data from carousel_data

    let showThumbs=false //no thumbnails in carousel
    let showCaptions=false //no captions on photos in carousel
</script>

<Center>
    <!-- create carousel of images -->
    <div class="scale-125 pt-10">
        <CarouselTransition {images} {showCaptions} {showThumbs} />
    </div>
</Center>