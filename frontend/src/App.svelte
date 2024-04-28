<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import JobCreate from "./routes/JobCreate.svelte"
  import Navigation from "./components/Navigation.svelte";
  import PasswordConfirm from "./routes/PasswordConfirm.svelte";
  import JobModify from "./routes/JobModify.svelte";

  const routes = {
    '/': Home,
    '/detail/:job_id/:page': Detail,
    '/job-create': JobCreate,
    '/password-confirm/:job_id/:page': PasswordConfirm,
    '/job-modify/:job_id/:page': JobModify,
  }
</script>

<Navigation />
<Router {routes}/>