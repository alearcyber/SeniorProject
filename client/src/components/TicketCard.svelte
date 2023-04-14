<!-- 
    Ticket Card Component
    This component is  on the page to buy tickets for a 
    specific event and is used to create the cards that 
    have each of the available tickets and their data.
-->

<script>
    // @ts-nocheck
    import { Card, Table, TableHead, TableBody, TableHeadCell, TableBodyCell, TableBodyRow } from "flowbite-svelte"

    export let section
    export let row
    export let seat
    export let price

</script>

<div class="">
    <Card>
        <!-- Table showing the location of the seat -->
        <Table noborder={true}>
            <TableHead
                class="text-lg text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400"
            >
                <TableHeadCell>SEC</TableHeadCell>
                <TableHeadCell>ROW</TableHeadCell>
                <TableHeadCell>SEAT</TableHeadCell>
            </TableHead>
            <TableBody>
                <TableBodyRow class="text-base text-center">
                    <TableBodyCell>{section}</TableBodyCell>
                    <TableBodyCell>{row}</TableBodyCell>
                    <TableBodyCell>{seat}</TableBodyCell>
                </TableBodyRow>
            </TableBody>
        </Table>

        <!-- Price of ticket and add to cart button -->
        <div class="flex content-center justify-end pt-6">
            <h1 class="text-lg">${price}</h1>
        </div>
    </Card> 
</div>
