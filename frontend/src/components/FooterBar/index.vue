<template lang="pug">
  v-footer.mt-6(color='#f57e2e' dark='')
    v-row.my-4.text-center(justify='center')
      v-col.pa-0(cols='12')
        | Lorem ipsum dolor sit amet consectetur
        | adipisicing elit.
      v-col.pa-0(cols='12')
        v-btn(v-for='icon in icons' :key='icon' text='' dark='')
          v-icon {{ icon }}
      v-col.pa-0(cols='12')
        v-divider.mt-1
      v-col.align-center(cols='12') © 2022 autoxuanphuc.com.vn
</template>

<script>
import {defineComponent} from "vue";

const FooterBar = defineComponent({
    setup() {
        const icons = [
            'mdi-facebook',
            'mdi-twitter',
            'mdi-instagram',
            'mdi-youtube',
        ]
        return {
            icons
        }
    }
})

export default FooterBar
</script>