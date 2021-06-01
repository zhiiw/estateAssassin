<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated className="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-icon name="house" />
          Houses
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs v-if="loggedIn" align="left">
        <q-route-tab to="/index" exact label="Home" icon="home"/>
        <q-route-tab to="/list" exact label="House list" icon="list"/>
        <q-route-tab to="/info" exact label="House info" icon="info"/>
        <q-route-tab to="/about" exact label="About us" icon="help"/>

        <q-tab label="Logout" @click="onLogout()" icon="logout"></q-tab>
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view/>
    </q-page-container>

    <q-footer reveal bordered className="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          All rights reserved. Copyright 2021.
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      loggedIn: false
    }
  },
  created() {
    this.loggedIn = sessionStorage.getItem('loggedIn') !== null
    const timer = setInterval(() => {
      this.checkLogin();
    }, 500)
  },
  methods: {
    onLogout() {
      console.log('logout')
      sessionStorage.removeItem('loggedIn')
      sessionStorage.removeItem('userid')
      sessionStorage.removeItem('role')
      this.loggedIn = false
      this.$router.replace('/')
    },
    checkLogin() {
      this.loggedIn = sessionStorage.getItem('loggedIn') !== null
      if(this.loggedIn) {
        if(this.$route.path === '/' || this.$route.path === '/reg')
          this.$router.push('/index')
      }
      else {
        if(this.$route.path !== '/' && this.$route.path !== '/reg')
          this.$router.push('/')
      }
    }
  }
}
</script>
