<template lang="pug">
  div
    v-dialog(
      no-click-animation
      persistent
      max-width="350"
      @keydown="onTyping"
      v-model="showDialog"
    )
      v-card
        v-card-title.green
          v-btn(v-if="isBack" icon dark @click="close()")
            v-icon mdi-keyboard-backspace

          span.white--text confirm dialog
          v-spacer
          portal-target(name="header-dialog-action")
          v-btn(icon dark @click="cancel()")
            v-icon mdi-close

        v-card-text.relative-card.pa-0
          v-row.ma-5.display-msg(justify="center")
            span(v-if="messages" v-for="msg in messages") {{ msg }}
        v-card-actions
          v-btn.relative-btn(
            width="50%"
            color="rough_black"
            @click="cancel()"
          )
            span.blue--text Cancel
          v-btn.relative-btn(
            width="50%"
            dark
            :color="colorConfirm"
            @click="ok()"
          )
            span.white--text OK
</template>

<script>
import {defineComponent} from 'vue'

const ConfirmDialog = defineComponent({
  props: {
    showDialog: {
      type: Boolean,
      required: true
    },
    messages: {
      type: Array,
      default: () => []
    },
    isBack: {
      type: Boolean,
      required: false,
      default: false
    },
    label: {
      type: String,
      default: '',
      required: false
    },
    colorConfirm: {
      type: String,
      default: 'green'
    }
  },
  setup(props, {emit}) {
    const cancel = () => {
      emit('on-cancel')
    }

    const ok = () => {
      emit('on-ok')
    }

    const onTyping = (event) => {
      if (event.keyCode === 27) {
        // Press ESC
        close()
      }
      if (event.keyCode === 13) {
        ok()
      }
    }

    return {
      cancel,
      ok,
      onTyping
    }
  }
})
export default ConfirmDialog
</script>
<style lang="sass" scoped>
.v-card
  ::v-deep .v-card__title
    position: sticky
    top: 0
    z-index: 999

  ::v-deep .v-card__actions
    position: sticky
    background-color: white
    bottom: 0
    z-index: 999

.display-msg
  display: inline-grid

.message
  font-weight: bold
  font-size: 15px

</style>