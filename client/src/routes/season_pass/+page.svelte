<!-- 
    Payment Page
    This page is where the customer will buy season passes
-->

<script>
// @ts-nocheck

    import Center from '../../layouts/center.svelte' //import Center layout
    import { Select, Label, Heading, P } from 'flowbite-svelte'
    let selected
    let seasons = [
        {value:"us", name: "United States"},
        {value:"ca", name: "Canada"},
        {value:"fr", name: "France"},
    ]
</script>

<Center>
    <Heading class="mb-4">Season Pass</Heading>
    <P class="mb-10">Buy a season pass to your favorite show!</P>
    <Label>Select a season
        <Select class="mt-2" items={seasons} bind:value={selected} />
    </Label>
</Center>