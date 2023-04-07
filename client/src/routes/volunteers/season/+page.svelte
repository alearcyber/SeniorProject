<!-- 
    Create Season Page
    This page is where the volunteers go to create a new season.
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList } from 'flowbite-svelte'

    let values=[{
       "title": "",
    }]; 
        
    const addField = () => {
       values = [...values, {title: ''}]
    };
        
    const removeField = () => {
       values = values.slice(0, values.length-1)
    };
</script>
  
<div class="mb-10 flex justify-center" >
    <form class="flex flex-col space-y-6" style="width:800px" action='/'>
        <!-- Title -->
        <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create New Season</h3>

        <!-- Season Name Field -->
        <Label class="space-y-2">
          <span>Season Name</span>
          <Input type="text" name="season_name" placeholder="" required />
        </Label>

        <!-- Organization Field -->
        <Label class="space-y-2">
          <span>Organization</span>
          <Input type="text" name="organization" placeholder="" required />
        </Label>

        <!-- Production Name Field -->
        {#each values as v, i}
        <div>
            <Label class="space-y-2">
                <span>Production Title</span>
                <Input type="text" name="production_name" bind:value={values[i].title} placeholder="" required />
            </Label>
        </div>
        {/each}
        {#if values.length >= 2}
        <Button style="width: 200px" color="light" on:click={removeField}>Remove Production -</Button>
        {/if}
        <Button style="width: 200px" color="dark" on:click={addField}>Add Production +</Button>


        <!-- Create Season button -->
        <Button type="submit" class="w-full1">Create Season</Button>
    </form>
  </div>
  
 



