<template lang="pug">
  v-row.ma-0.pa-0
    v-col.pa-1.ma-0(
      class="child-flex"
      cols="3"
      v-for="image in listImage"
      :key="image.url"
    )
      v-img.rounded-lg(
        aspect-ratio="1"
        class="grey lighten-2"
        :src="image.url"
        disable-ssl
      )
        template(v-slot:placeholder)
          v-row(
            class="fill-height ma-0"
            align="center"
            justify="center"
          )
            v-progress-circular(
              indeterminate
              color="grey lighten-5"
            )
        div.image-delete-label(v-if="!readonly" @click="removeImage(image)")
          span.white--text.caption remove image

    v-col.pa-1.image-container(
      v-if="!readonly"
      class="d-flex child-flex"
      :cols="listImage.length ? 3 : 12"
    )
      v-row.ma-0.pa-0.add-new-image(
        align="center"
        justify="center"
        @click="selectImage"
      )
        v-progress-circular(
          v-if="isUpload"
          indeterminate
          color="black lighten-5"
        )
        span.add-new-image__title(v-else)
          v-icon mdi-camera-outline
          br
          span.caption add new image

        input(
          multiple
          hidden
          ref="refInput"
          type="file"
          accept="image/*"
          @change="uploadImages"
        )
</template>

<script lang="js">
import { defineComponent, watch, ref } from 'vue'
import { readFile } from '@/utils'


const ImageList = defineComponent({
  props: {
    images: {
      type: Array,
      required: false,
      default: () => []
    },
    max: {
      type: Number,
      required: false,
      default: 100
    },
    readonly: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup(props, { emit }) {
    const isUpload = ref(false)
    const listImage = ref(props.images.filter(img => img.url))
    const refInput = ref(null)
    const selectImage = () => {
      if (isUpload.value === false) {
        refInput.value.click()
      }
    }

    const uploadImages = async () => {
      const files = refInput.value.files ? Object.values(refInput.value.files) : []
      const body = await Promise.all(
        files.map(async (file) => {
          const payload = await readFile(file)
          return {
            payload,
            id: null,
            name: file.filename,
            type: file.type,
            size: file.filesize,
            url: URL.createObjectURL(file)
          }
        })
      )
      listImage.value = [...listImage.value, ...body]
      emit('on-change', listImage.value)
    }
    const removeImage = (image) => {
      const { url } = image
      listImage.value = listImage.value.filter((i) => i.url !== url)
      emit('on-change', listImage.value)
      if (image.id) {
        emit('on-remove', image.id)
      }
    }

    const refresh = () => {
      listImage.value = []
    }

    watch(
      () => props.images,
      () => {
        refresh()
        listImage.value = [...props.images].filter(img => img.url)
          console.log(listImage.value, 11)
      }
    )

    return {
      isUpload,
      listImage,
      refInput,
      selectImage,
      uploadImages,
      removeImage
    }
  }
})

export default ImageList
</script>

<style scoped lang="sass">
.image-container
  min-height: 85px

.image-delete-label
  display: flex
  justify-content: center
  align-items: center
  position: absolute
  bottom: 0
  width: 100%
  background-color: red
  opacity: 0.5
  cursor: pointer

.add-new-image
  border-radius: 8px
  border-width: 2px
  border-style: dotted

.add-new-image__title
  text-align: center
</style>
