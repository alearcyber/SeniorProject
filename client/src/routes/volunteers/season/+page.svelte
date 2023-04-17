<!-- 
    Create Season Page
    This page is where the volunteers go to create a new season.
-->

<script>
    import { Label, Input, Button, Listgroup, Checkbox } from 'flowbite-svelte'
    import { onMount } from 'svelte';

    onMount(async () => {
		console.log('This is onMount for the Create Season page');
		console.log(get_production_list());
	});

    //hard coded event data that will eventually be received from database
    let list = [
        { name: "Phantom of the Opera"
        },
        { name: "Hamilton"
        },
        { name: "Wicked"
        },
    ]

    async function get_production_list() {
        let email = sessionStorage.getItem("user");
        let org_id = sessionStorage.getItem("org_id");
        console.log(email, org_id);

        let response = await fetch(`http://127.0.0.1:5000/get_productions/${email}:${org_id}`);
        const out = await response.json();
        console.log(out);
        list = out;
        return out;
    }
    
    

    
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
            {#each list as item, i}

                <div class="d-flex justify-space-around">
                    <Checkbox group={selected} value={item.name}/> {item}<br>
                </div>
            {/each}   
        </Label>

        
        <!-- Create Season button -->
        <Button type="submit" class="w-full1">Create Season</Button>
    </form>
  </div>
  
 



