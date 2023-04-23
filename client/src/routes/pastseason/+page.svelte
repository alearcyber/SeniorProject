<script>
    import { Button, Input, Heading } from 'flowbite-svelte'
    import { onMount } from 'svelte'
    import Center from '../../layouts/center.svelte' //import Center layout

    //check that the user is logged in
    let email = '';
    onMount(async () => {
        populate_season_pass_info();
        let val = sessionStorage.getItem('user');
		if (val !== null) {
			email = val
		}
    });

    //logical storage of the season passes in memory
    let season_pass_info = []
    let season_pass_state = {}

    //this function populates the season apss info when the page loads
    async function populate_season_pass_info(){
        let data = {}
        try {
            const response = await fetch('http://127.0.0.1:5000/get_season_pass_info', {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'email': email})
            })

            data = await response.json()
        } catch (error) {
            console.error({ error })
            data = {
                season_passes: [
                    {'id':1, 'email': 'ojhn@gmail.com', 'name': 'johntravolta', 'address': 'the road'},
                    {'id':2, 'email': 'one', 'name': 'two', 'address': 'three'},
                    {'id':3, 'email': 'asdfasdf', 'name': 'asdfasdf', 'address': 'twerf'},
                ]
            }
        } 
        
        season_pass_info = data.data?.season_passes ?? data.season_passes

        season_pass_info.forEach((item) => {
            season_pass_state[item.id] = false;
        })
    }

    //this function updates the information for the database
    async function handle_submit(card) {
        // call your function with the form data as arguments
        console.log({ card })

        const response = await fetch('http://127.0.0.1:5000/update_season_pass_info', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(card)
        })

        const data = await response.json()

        console.log({ data, response })
    }

    function handleInput(card) {
        season_pass_state[card.id] = true
    }

    function cardDisabled(card){
      return season_pass_state[card.id] === false
    }
</script>

<Center>
    <Heading>Past Season Pass Info</Heading>
</Center>

<div>
    {#each season_pass_info as card}
        <div class="p-1 flex items-center justify-center w-100 text-center">
            <div class="card flex flex-col max-w-6xl justify-start">
                <div class="text-center font-bold text-lg">
                    Season Pass
                </div>
                <form
                    class="grid grid-cols-7 gap-2"
                >
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="col-span-2">
                        Email:
                        <Input
                            name="email"
                            type="text" 
                            bind:value={card.email}
                            on:input={handleInput(card)}
                        />
                    </label>

                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="col-span-2">
                        Name:
                        <Input 
                            name="name" 
                            type="text" 
                            bind:value={card.name} 
                            on:input={handleInput(card)}
                        />
                    </label>

                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="col-span-2">
                        Address:
                        <Input 
                            name="address" 
                            type="text" 
                            bind:value={card.address} 
                            on:input={handleInput(card)}
                        />
                    </label>
                    <div class="inline-flex items-bottom justify-start">
                        <Button 
                            type="submit" 
                            disabled={cardDisabled(card)}
                            on:click={handle_submit(card)}
                            class="h-10 mt-6"
                        >
                            Save
                        </Button>
                    </div>
                </form>
            </div>
        </div>
    {/each}
</div>

<style>
    .card {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        margin: 10px;
        box-shadow: inset 0 0 0 0 transparent;
    }

    .selected {
        background-color: #e6f7ff;
        border: 1px solid #1890ff;
    }
</style>