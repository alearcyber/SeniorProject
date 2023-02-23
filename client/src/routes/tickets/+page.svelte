<script>
    import { Listgroup, Button } from "flowbite-svelte";
     let list = [
      { name: "Phantom of the Opera", date: "May 3", time: "6:00 p.m.", venue: "Civic Center Playhouse"
      },
      { name: "Hamilton", date: "May 7", time: "6:00 p.m.", venue: "Civic Center Concert Hall"
      },
      { name: "Wicked", date: "May 8", time: "6:00 p.m.", venue: "Civic Center Playhouse"
      },
    ];
  </script>
<div class="block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
    <div class="flex justify-between items-center mb-4">
        <h1 class="text-2xl font-bold leading-none text-blue-500 dark:text-white">Events</h1>
    </div>
    <Listgroup items={list} let:item class="border-0 dark:!bg-transparent">
      <div class="flex items-center space-x-4">
        <div class="inline-flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
            {item.date}
        </div>
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
        <Button class="w-fit" href="/seats">
            Buy tickets <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 ml-2"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" /></svg>
        </Button>
      </div>
    </Listgroup>
</div>