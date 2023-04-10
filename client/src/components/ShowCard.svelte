<!-- 
    Show Card Component
    This component is used on the Shows page to create the cards that
    have each of the upcoming shows and their data.
-->

<script>
    /**
    * imgURL is type String
	* @type {String}
	*/
    export let imgUrl

    /**
    * imgTitle is type String
	* @type {String}
	*/
    export let imgTitle = 'image'
</script>

<!-- Create cards -->
<div class="block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
    <slot name="layout">
        <div class="flex justify-between space-x-5">
            {#if imgUrl} 
                <!-- format image -->
                <img class="rounded-lg" src={imgUrl} alt={imgTitle} title={imgTitle} width="150px" height="200px"/>
            {/if}
            <slot />
        </div>
    </slot>
</div>
