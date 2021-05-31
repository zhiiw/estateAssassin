<template>
  <div>
    <q-card class="absolute-center" style="width: 50%">
      <q-img
        src="https://cdn.quasar.dev/img/parallax1.jpg"
        basic
        style="height: 400px"
      />
      <p class="text-h1 text-weight-bold q-my-lg q-mx-md text-center">Welcome, &nbsp;{{username}}!&nbsp; <q-badge v-if="isAdmin" class="text-subtitle1" color="primary"> Admin</q-badge> </p>
      <br>
      <q-card-section class="q-mx-md">
        <p class="text-h3 text-primary text-weight-bolder">Wanting a house?</p>
        <p class="text-h4">Why not buy a <q-badge class="text-h4">{{ random_house_decoration }}</q-badge> house with <q-badge class="text-h4">{{ random_house_unit_type}}</q-badge> at the price of
          <q-badge class="text-h4">{{ random_house_price }} W</q-badge> ?         <q-btn class="float-right" color="primary" size="lg" push @click="goRandom()">Let's go!</q-btn>
        </p>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'PageIndex',
  data() {
    return {
      loggedIn: false,
      username: '',
      user_id: -1,
      isAdmin: false,
      random_house_decoration: '...',
      random_house_unit_type: '...',
      random_house_price: 0,
      random_house_id: -1
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    if(this.loggedIn) {
      if(this.$route.path === '/' || this.$route.path === '/reg')
        this.$router.push('/index')
    }
    else {
      if(this.$route.path !== '/' && this.$route.path !== '/reg')
        this.$router.push('/')
    }
    this.username = sessionStorage.getItem('loggedIn')
    this.user_id = sessionStorage.getItem('user_id')
    this.isAdmin = sessionStorage.getItem('role') === '1'
  },
  mounted() {
    let _this = this
    this.$axios.get('http://192.168.31.115:8000/api/random').then(function (response) {
      console.log(response)
      let res = response.data
      _this.random_house_decoration = res.decoration
      _this.random_house_price = res.price
      _this.random_house_unit_type = res.unit_type
      _this.random_house_id = res.house_id
    })
  },
  methods: {
    goRandom() {
      this.$router.push({name: 'info', params: {id: this.random_house_id}})
    }
  }
}
</script>
