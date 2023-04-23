<script>
  import {onMount} from "svelte";
  import { SeatStore, sum } from '../stores/SeatStore.js'
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte'

  let there_is_an_exchange = false;
  let exchange_price = 0;

  //on mount function
  onMount(async () => {
    //set exchange variables
    if(sessionStorage.getItem('exchange') === null){ //there is no info to exchange
      there_is_an_exchange = false;
      exchange_price = 0;
    } else { //there is an exchange to be made, tally up price
      there_is_an_exchange = true;
      let pairs = sessionStorage.getItem('exchange').split(';');
      for(let i = 0; i < pairs.length; i++){
        exchange_price = exchange_price + parseInt(pairs[i].split(',')[1])
      }
    }

  });

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
        {#if there_is_an_exchange}
          <TableBodyRow>
            <TableBodyCell class="capitalize">Exchanged Tickets...</TableBodyCell>
            <TableBodyCell>- ${exchange_price}</TableBodyCell>
          </TableBodyRow>
        {/if}
      </TableBody>
      <tfoot>
        <tr class="font-semibold text-gray-900 dark:text-white">
          <th scope="row" class="py-3 px-6 text-base">Total</th>
          {#if there_is_an_exchange}
            {#if ($sum - exchange_price) > 0}
              <td class="py-3 px-6">${$sum - exchange_price}</td>
            {:else}
              <td class="py-3 px-6">$0</td>
            {/if}
          {:else}
            <td class="py-3 px-6">${$sum}</td>
          {/if}
        </tr>
      </tfoot>
    </Table>
</div>