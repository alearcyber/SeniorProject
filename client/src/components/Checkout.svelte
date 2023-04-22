<script>
  import { SeatStore, sum } from '../stores/SeatStore.js'
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte'

  /**
   * @type {any[]}
   */
  let mySeatStore
  $: mySeatStore = $SeatStore //subscribe to seat store
</script>

<div class="bg-gray-200 p-4 rounded-lg shadow-md max-h-96 overflow-auto">
    <h1 class="text-2xl font-bold mb-2">Checkout</h1>
    <Table noborder={true}>
      <TableHead
        class="text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400"
      >
        <TableHeadCell>Ticket</TableHeadCell>
        <TableHeadCell>Price</TableHeadCell>
      </TableHead>
      <TableBody>
        {#each mySeatStore as { sec, row, seat, price } }
          {#if seat}
            <TableBodyRow>
              <TableBodyCell class="capitalize">{sec.replace('_', ' ')} - Seat {row}{seat} </TableBodyCell>
              <TableBodyCell>${price}</TableBodyCell>
            </TableBodyRow>
          {/if}
        {/each}
      </TableBody>
      <tfoot>
        <tr class="font-semibold text-gray-900 dark:text-white">
          <th scope="row" class="py-3 px-6 text-base">Total</th>
          {#if $sum >= 0}
            <td class="py-3 px-6">${$sum}</td>
          {:else}
            <td class="py-3 px-6">$0</td>
          {/if}
        </tr>
      </tfoot>
    </Table>
</div>