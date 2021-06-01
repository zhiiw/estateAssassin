<template>
  <div>
    <q-card class="q-mx-auto q-mt-xl" style="width: 50%">
      <q-img
        src="https://cdn.quasar.dev/img/parallax1.jpg"
        basic
        style="height: 400px"
      />
      <p class="text-h1 text-weight-bold q-my-lg q-mx-md text-center">House&nbsp;#{{id}}</p>
      <br>
      <q-card-section class="q-mx-md q-my-xl">
        <q-list>
          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="primary" name="explore" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Toward </q-item-label>
              <q-item-label class="text-h5" primary> {{toward}} </q-item-label>
            </q-item-section>
          </q-item>

          <br>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="orange" name="money" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Unit price </q-item-label>
              <q-item-label class="text-h5" primary> ¥{{ unit_price }} </q-item-label>
            </q-item-section>
          </q-item>

          <br>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="red" name="fullscreen_exit" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Building area </q-item-label>
              <q-item-label class="text-h5" primary> {{ building_area }} m² </q-item-label>
            </q-item-section>
          </q-item>

          <br>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="green" name="credit_card" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Total price </q-item-label>
              <q-item-label class="text-h5" primary> ¥{{ total_price }} W </q-item-label>
            </q-item-section>
          </q-item>

          <br>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="purple" name="chair" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Decoration </q-item-label>
              <q-item-label class="text-h5" primary> {{ decoration }} </q-item-label>
            </q-item-section>
          </q-item>

          <br>

          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="amber" name="stairs" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Floor </q-item-label>
              <q-item-label class="text-h5" primary> {{ floor }} </q-item-label>
            </q-item-section>
          </q-item>

          <br>
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="grey" name="cottage" style="font-size: 60px"/>
              </q-item-section>

              <q-item-section>
                <q-item-label class="text-h4 text-weight-bold"> Unit Type </q-item-label>
                <q-item-label class="text-h5" primary> {{ unit_type }} </q-item-label>
              </q-item-section>
            </q-item>
          <br>
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="yellow" name="account_circle" style="font-size: 60px"/>
              </q-item-section>

              <q-item-section>
                <q-item-label class="text-h4 text-weight-bold"> Intermediary </q-item-label>
                <q-item-label class="text-h5" primary> {{ intermediary_name }} </q-item-label>
              </q-item-section>
            </q-item>
          <br>
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="pink" name="call" style="font-size: 60px"/>
              </q-item-section>

              <q-item-section>
                <q-item-label class="text-h4 text-weight-bold"> Phone Number </q-item-label>
                <q-item-label class="text-h5" primary> {{ phone }} </q-item-label>
              </q-item-section>
            </q-item>
          <br>
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="blue" name="place" style="font-size: 60px"/>
              </q-item-section>

              <q-item-section>
                <q-item-label class="text-h4 text-weight-bold"> Area </q-item-label>
                <q-item-label class="text-h5" primary> {{ area }} </q-item-label>
              </q-item-section>
            </q-item>
          <br>
            <q-item clickable>
              <q-item-section avatar>
                <q-icon color="cyan" name="local_library" style="font-size: 60px"/>
              </q-item-section>

              <q-item-section>
                <q-item-label class="text-h4 text-weight-bold"> Community </q-item-label>
                <q-item-label class="text-h5" primary> {{ community_name }} </q-item-label>
              </q-item-section>
            </q-item>
        <br>
          <q-item clickable>
            <q-item-section avatar>
              <q-icon color="yellow" name="cabin" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Part Area </q-item-label>
              <q-item-label class="text-h5" primary> {{ part_area }} </q-item-label>
            </q-item-section>
          </q-item>

          <br>
          <q-item v-if="case_type===''" clickable>
            <q-item-section avatar>
              <q-icon color="green" name="verified" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> <q-badge class="text-h4" color="green">No Crime</q-badge></q-item-label>
            </q-item-section>
          </q-item>

          <q-item v-else clickable>
            <q-item-section avatar>
              <q-icon color="black" name="favorite" style="font-size: 60px"/>
            </q-item-section>

            <q-item-section>
              <q-item-label class="text-h4 text-weight-bold"> Case </q-item-label>
              <q-item-label class="text-h5" primary> {{ case_type }} * {{ case_time }} 件 </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "Info",
  data () {
    return {
      id: 1230,
      toward: '',
      unit_price: 0,
      building_area: 0,
      total_price: 0,
      decoration: '',
      floor: '1',
      unit_type: '',
      intermediary_name: '',
      phone: 0,
      area: '',
      community_name: '',
      part_area: '',
      case_type: '',
      case_time: 0,
      loggedIn: false,
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
    if(this.$route.params.id !== undefined)
      this.id = this.$route.params.id
    let _this = this
    this.$axios.get('http://127.0.0.1:8000/api/get_id/' + this.id).then(function (response) {
      let res = response.data
      if(res.status === "Success") {
        _this.toward = res.toward
        _this.unit_price = res.unit_price
        _this.building_area = res.building_area
        _this.total_price = res.total_price
        _this.decoration = res.decoration
        _this.floor = res.floors
        _this.unit_type = res.unit_type
        _this.intermediary_name = res.intermediary_name
        _this.phone = res.phone
        _this.area = res.area
        _this.community_name = res.community_name
        _this.part_area = res.part_area
        _this.case_type = res.case_type
        _this.case_time = res.case_times
      } else {
        _this.$q.notify({
          type: 'negative',
          message: 'Login error: ' + res.message
        })
      }
    }).catch(function (error) {
      console.log(error)
      _this.$q.notify({
        type: 'negative',
        message: 'Internal error.'
      })
    })
  },

}
</script>

<style scoped>

</style>
