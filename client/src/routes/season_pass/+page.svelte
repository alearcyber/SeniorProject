<!-- 
    Payment Page
    This page is where the customer will buy season passes
-->

<script>
// @ts-nocheck
    import Center from '../../layouts/center.svelte' //import Center layout
    import { Select, Label, Heading, P } from 'flowbite-svelte'
    import ShowsPerSeason from '../../components/ShowsPerSeason.svelte'
    
    export let seasons
    let selected
</script>

<Center>
    <Heading class="mb-4">Season Pass</Heading>
    <P class="mb-10">Buy a season pass to your favorite show!</P>
    <Label>Select a season
        <Select class="mt-2" items={seasons} bind:value={selected}/>
    </Label>
</Center>

<ShowsPerSeason />
