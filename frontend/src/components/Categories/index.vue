<template lang="pug">
  //v-card.mx-auto(max-width='300' tile='')
  .border.width-card
    v-list(dense='')
      v-subheader {{ title }}
      v-list-item-group(v-model='selectedItem' color='#f57e2e')
        v-list-item(v-for='(item, i) in items' :key='i' @click="gotoProductsPage(item)")
          v-img(:src='item.logo.url' max-width="25" )
          span.pl-2.font-size-12 {{ item.text }}

</template>

<script>
import router from "@/router";
import {urlPath} from '@/utils'

const Categories = {
  props: {
    title: {default: ''},
    selectedItem: {default: 0},
    items: {default: () => []}
  },
  data() {
    return {}
  },
  methods: {
    gotoProductsPage(catName) {
      router.push({
        name: urlPath.Products.name,
        params: {categoryName: catName.name}
      }).catch((e) => {
        return
      })
    }
  }
}

export default Categories
</script>

<style scoped lang="sass">
.border
  //border-radius: 15px
  border: 2px solid #f57e2e
.width-card
  max-width: 250px
.font-size-12
  font-size: 12px
</style>