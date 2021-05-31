
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/Login.vue') },
      { path: '/reg', component: () => import('pages/Register')},
      { path: '/index', component: () => import('pages/Index.vue') },
      { path: '/info', name: 'info', component: () => import('pages/Info.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
