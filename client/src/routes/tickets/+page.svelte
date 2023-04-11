<!-- 
    Tickets Page
    This page is where the upcoming events will appear as a list including their 
    date, time, and venue. It includes a button with a link to the page where the 
    customer will select their seat for the given event. 
-->

<script>
// @ts-nocheck

  import { Listgroup, Button, Heading } from "flowbite-svelte"


  // grab data from the database
  export let data;
  let list = data.data;


  //display correct venue graphic
  function href(item) {
    return item.venue === 'Civic Center Concert Hall' 
      ? `/concert_seats?id=${item.performance_id}`
      : `/playhouse_seats?id=${item.performance_id}`
  }
</script>

<!-- Title -->
<Heading tag="h1" class="mb-4 text-blue-500" customSize="text-3xl font-extrabold  md:text-4xl lg:text-5xl">
  Events
</Heading>

<!-- List of events -->
<Listgroup items={list} let:item class="border-0 dark:!bg-transparent">
  <div class="flex items-center space-x-4">

    <!-- format date of event -->
    <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
      {item.date}
    </div>

    <!-- format name, venue, and time of event -->
    <div class="flex-1 min-w-0">
      <p class="text-xl font-medium text-gray-900 truncate dark:text-white">
        {item.name}
      </p>
      <p class="text-base text-gray-500 truncate dark:text-gray-400">
        {item.venue}
      </p>
      <p class="text-base text-gray-500 truncate dark:text-gray-400">
        {item.time}
      </p>
    </div>

    <!-- Button linking to Seats page -->
    <Button class="w-fit" href={href(item)}>
      Buy tickets
    </Button>
  </div>
</Listgroup>