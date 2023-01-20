<script>
    /**
	 * @type {String}
	 */
     export let imgUrl
    /**
	 * @type {String}
	 */
     export let imgTitle = 'image'
</script>

<div class="block max-w-50rem p-6 bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
    <slot name="layout">
        <div class="flex justify-between space-x-5">
            {#if imgUrl}
                <img class="rounded-lg" src={imgUrl} alt={imgTitle} title={imgTitle} />
            {/if}
            <slot />
        </div>
    </slot>
</div>
