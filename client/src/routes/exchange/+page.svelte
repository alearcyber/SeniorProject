<script>

    //get url params
    import { page } from '$app/stores';
    const url = $page.url;  //url
    const number = url.searchParams.get('number')


    //continue on to selecting a seat
    function keep_going(){
        //TODO
    }


    //user clicks the button to indicate they want to exchange tickets
    function wants_to_exchange(){
        //TODO
    }



</script>


<style>

    h1 {
        font-size: 50px;
    }
    button {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    color: #fff;
    background-color: #4caf50;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #3e8e41;
  }
</style>

<h1>Would you like to exchange a ticket?</h1>
<div>
  <button on:click={wants_to_exchange}>Yes</button>
  <button on:click={keep_going}>No</button>
</div>