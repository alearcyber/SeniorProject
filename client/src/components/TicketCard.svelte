<script>
// @ts-nocheck

    import { Button, Card, Table, TableHead, TableBody, TableHeadCell, TableBodyCell, TableBodyRow } from "flowbite-svelte"

    export let section
    export let row
    export let seat
    export let price
</script>

<Card>
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
    <div class="flex content-center justify-between pt-6">
        <h1 class="text-lg">${price}</h1>
        <Button class="w-24" size="sm">Buy</Button>
    </div>
</Card> 