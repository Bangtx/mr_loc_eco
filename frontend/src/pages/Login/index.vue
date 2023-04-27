<template lang="pug">
  .pt-10
    v-card(class="mx-auto" max-width="344" )
      v-card-title.bg.white--text(color="#f57e2e" ) Đăng nhập
      v-card-text
        v-text-field(label="mssv" v-model="info.code")
        v-text-field(label="password" v-model="info.password" type="password" )
      v-card-actions
        v-row
          v-col(cols="12")
            v-btn.white--text(width="100%" color="#f57e2e" @click="onLogin") Đăng nhập

</template>

<script>
import {defineComponent, getCurrentInstance, onMounted, ref} from "vue";
import {createData, urlPath} from '@/utils'
import ForgotPass from "@/pages/Login/ForgotPass.vue";

const Login = defineComponent({
  components: {ForgotPass},
  setup() {
    const instance = getCurrentInstance().proxy
    const {$router, $store, $toast} = instance
    const info = {
      code: null,
      password: null
    }

    const onLogin = async () => {
      // const data = await createData('/user/login/', info, false)
      if (info.code === 'admin@gmail.com' && info.password === 'admin123') {
        localStorage.setItem('login', true)
        await $router.push({name: 'Admin'})
        // $store.commit("setShowAppBar", true)
      } else {
        $toast.error('Login failed')
      }
    }

    onMounted(() => {
      $store.commit("setShowAppBar", false)
    })

    return {
      info,
      onLogin,
    }
  }
})
export default Login
</script>

<style lang="sass" scoped>
.bg
  background-color: #f57e2e
</style>