<!-- 
    Shows Page
    This page is where the upcoming events will appear in individual cards with 
    their title, image, and description. 
-->

<script>
    import { Button, Heading } from "flowbite-svelte"
    import Center from '../../layouts/center.svelte' //import Center layout

    /**
     * 'data' is assigned by the JS in page.js, which makes an API call to retun the JSON info. The 'shows' value is a
     * list of the upcoming shows.
     */
    //export let data;
    //const shows = data.shows;


    import { events } from '../../show_data/+server.js' //import show_data file
    import ShowCard from "../../components/ShowCard.svelte" //import showcard indicator
</script>

<Center>
    <div class="space-y-10">
        <!-- Title -->
        <Heading tag="h1" class="mb-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Upcoming Shows</Heading>

        <!-- Iterate through event data and place into individual cards -->
        {#each shows as { name, imgurl, description } }
            <article>
                <ShowCard imgUrl={imgurl} imgTitle={name}>
                    <div class="flex flex-col justify-between items-center ">
                        <!-- format event name -->
                        <h4 class="mb-2 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">{name}</h4>

                        <!-- format event description -->
                        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
                            {description}
                        </p>

                        <!-- Button linking to Tickets page -->
                        <Button class="w-fit" href="/tickets">
                            Buy tickets <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 ml-2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" /></svg>
                        </Button>
                    </div>
                </ShowCard>
            </article>
        {/each}
    </div>
</Center>