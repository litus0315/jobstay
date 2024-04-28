<script>
// @ts-nocheck
    import { link } from 'svelte-spa-router'
    import fastapi from "../lib/api"    
    import { pageStore } from '../lib/store';

    export let params = {}
    let job_id = params.job_id
    let page = params.page
    let job = {answers:[]}

    function get_job() {
        fastapi("get", "/api/job/detail/" + job_id, {}, (json) => {
            job = json
        })
    }

    get_job()

    pageStore.set(parseInt(page));
    


</script>

<div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">{job.subject}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="display: flex; align-items: center; white-space: pre-line; margin-bottom:20px; color:#6a6a6a; font-size: 13px;">
                <i class="material-icons" style="margin-right: 5px; color:#007ec6;">place</i> {job.sido} > {job.gugun}
            </div>
            <div class="card-text" style="white-space: pre-line;">
                {job.content}<br /><br />
                * 잡스테이에서 보았다고 말씀해주세요
            </div>
        </div>
    </div>
    <div class="row start align-items-center justify-content-center mt-3">
        <div class="col-auto"> <a href={`/`} use:link class="btn btn-primary">뒤로</a></div>
        <div class="col-auto"> <a href="/job-modify/{job.id}/{page}" use:link class="btn btn-primary">수정하기</a></div>
    </div>
</div>