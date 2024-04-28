<script>
    import { link } from 'svelte-spa-router'
    import JobModify from "../routes/JobModify.svelte";
</script>

<!-- 네비게이션바 -  green : #03C75A -->
<nav class="navbar navbar-expand-sm navbar-dark" style="background-color:#007ec6">
    <div class="container-fluid">
        <div class="col-sm-4">
                    <a class="navbar-brand" href="/" style="color: whitesmoke; font-size: 20pt;">
            <img src="/image/jobstay_logo.png" style="width:50px; height:50px; margin-right:5px;" alt="logo">
            <b>잡스테이</b>
        </a>
        </div>
        <div class="col-sm-4">
        <a class="navbar-brand" href="/"><a use:link href="/job-create" class="btn btn-outline-secondary" style="width:100%;background-color: #efefef;color:black;"><b>구인 등록</b></a></a>
        </div>
        <div class="col-sm-4">
            <ul class="navbar-nav">
                <li class="nav-item">

                </li>
            </ul>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>



<!--        <div class="collapse navbar-collapse" id="collapsibleNavbar">-->
<!--            <ul class="navbar-nav">-->
<!--                <li class="nav-item">-->
<!--                    <a use:link href="/job-create">-->
<!--                    <img src="/image/flag_korea.png" style="width:50px; margin-top:3px;">-->
<!--                    </a>-->
<!--                </li>-->
<!--                <li class="nav-item">-->
<!--                    <a use:link href="/job-create">-->
<!--                        <img src="/image/flag_korea.png" style="width:50px; margin-top:3px;">-->
<!--                    </a>-->
<!--                </li>-->
<!--            </ul>-->
<!--        </div>-->
    </div>
</nav>

