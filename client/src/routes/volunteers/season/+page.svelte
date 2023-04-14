<!-- 
    Create Season Page
    This page is where the volunteers go to create a new season.
-->

<script>
    import { Label, Input, Button, Listgroup, Checkbox } from 'flowbite-svelte'
    
    //hard coded event data that will eventually be received from database
    let list = [
        { name: "Phantom of the Opera"
        },
        { name: "Hamilton"
        },
        { name: "Wicked"
        },
    ]

    
    let selected = [""];
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

        <!-- Production List -->
        <Label class="space-y-2">
        <span> Production List</span>
            {#each list as item}
                <div class="d-flex justify-space-around">
                    <Checkbox bind:group={selected} value={item.name}/> {item.name}<br>
                </div>
            {/each}   
        </Label>

        
        <!-- Create Season button -->
        <Button type="submit" class="w-full1">Create Season</Button>
    </form>
  </div>
  
 



