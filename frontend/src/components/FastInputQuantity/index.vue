<template lang="pug">
  div
    div.btn.pa-2(@click="$emit('change-value', '-')")
      v-icon mdi-minus
    div.input.pa-2 {{ value }}
    div.btn.pa-2(@click="$emit('change-value', '+')")
      v-icon mdi-plus
</template>

<script>
const FastInputQuantity = {
  props: ['value']
}

export default FastInputQuantity
</script>

<style scoped lang="sass">
.btn
  width: 40px
  border: 1px solid #f57e2e
  float: left
  text-align: center
  cursor: pointer
.btn:active
  background-color: #ffc7a5
.input
  width: 80px
  border: 1px solid #f57e2e
  float: left
  text-align: right
</style>