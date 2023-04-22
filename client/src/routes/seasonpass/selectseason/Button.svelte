<script>
  export let to = '/';
  export let text = 'Click me';

  function handleClick() {
    window.location.href = to;
  }
</script>

<button on:click={handleClick}>{text}</button>
