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
        // shows data here
    const shows = [
            {
                id: 0,
                name: "Phantom of the Opera",
                imgurl: 'https://imaging.broadway.com/images/poster-178275/w230/222222/121277-1.jpg',
                description: "The longest-running show in Broadway history, Andrew Lloyd Webber’s The Phantom of the Opera debuted in 1988, winning seven Tony Awards® including Best Musical. Based on Gaston Leroux’s horror novel, it tells the enticing story of the Phantom, who haunts the stage of the Paris Opera and subsequently falls in love with a beautiful young soprano. Audiences are in for a thrilling night at the theater to see this timeless tale, accompanied by an unforgettable musical score.",
            },
            {
                id: 1,
                name: "Aladdin",
                imgurl: 'https://imaging.broadway.com/images/poster-178275/w230/222222/111616-4.jpg',
                description: "In the middle-eastern town of Agrabah, Princess Jasmine is feeling hemmed in by her father’s desire to find her a royal groom. Meanwhile, the Sultan’s right-hand man, Jafar, is plotting to take over the throne. When Jasmine sneaks out of the palace incognito, she forms an instant connection with Aladdin, a charming street urchin and reformed thief. After being discovered together, Aladdin is sentenced to death, but Jafar saves him by ordering him to fetch a lamp from the Cave of Wonders. Where there’s a lamp, there’s a Genie, and once Aladdin unwittingly lets this one out, anything can happen! Will Aladdin’s new identity as “Prince Ali” help him win Jasmine’s heart and thwart Jafar’s evil plans? Will the Genie’s wish for freedom ever come true?",
            },
            {
                id: 2,
                name: "The Book of Mormon",
                imgurl: 'https://imaging.broadway.com/images/poster-178275/w230/222222/121297-3.jpg',
                description: "The Book of Mormon follows two young missionaries who are sent to Uganda to try to convert citizens to the Mormon religion. One missionary, Elder Price, is an enthusiastic go-getter with a strong dedication to his faith, while his partner, Elder Cunningham, is a socially awkward but well meaning nerd whose tendency to embroider the truth soon lands him in trouble. Upon their arrival in Africa, Elders Price and Cunningham learn that in a society plagued by AIDS, poverty and violence, a successful mission may not be as easy as they expected.",
            },
            {
                id: 3,
                name: "Sweeney Todd",
                imgurl: 'https://imaging.broadway.com/images/poster-178275/w230/222222/123245-11.jpg',
                description: "Stephen Sondheim and Hugh Wheeler’s landmark musical tells the tale of a resourceful pie shop owner and a vengeful barber out for blood. After he’s sent away by a corrupt judge, Sweeney returns to London years later seeking his long-lost family, and forms an unlikely partnership with Mrs. Lovett, who serves up pies underneath his former shop. Together, they wreak havoc on Fleet Street and serve up the hottest – and most unsettling – pies in London.",
            },
        ];
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


    <div style = "position:relative; top:100px; background-color:yellow;">
        <!-- Button for buying season pass -->
        <Heading tag="h1" class="mb-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">WANT A SEASON PASS!?!?!</Heading>
        <Button class="w-fit" href="/seasonpass/selectseason">
            Click Here To Check It Out
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                 stroke="currentColor" class="w-5 h-5 ml-2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>
            </svg>
        </Button>
    </div>
</Center>