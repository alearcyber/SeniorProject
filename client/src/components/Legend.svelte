<script>
    import { Card, Indicator } from "flowbite-svelte"
</script>

<Card class="absolute max-w-xs">
    <h1 class="font-bold text-black">
        Legend
    </h1>
    <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white">
        <span class="flex w-2.5 h-2.5 bg-blue-600 rounded-full mr-1.5 flex-shrink-0">
        </span>
        Available
    </span>
    <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white">
        <span class="flex w-2.5 h-2.5 bg-stone-500 rounded-full mr-1.5 flex-shrink-0">
        </span>
        Unavailable
    </span>
    <span class="flex items-center text-sm font-medium text-gray-900 dark:text-white">
        <span class="flex w-2.5 h-2.5 bg-lime-500 rounded-full mr-1.5 flex-shrink-0">
        </span>
        Selected
    </span>
</Card>