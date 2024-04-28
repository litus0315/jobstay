<script>
import fastapi from "../lib/api";
import { link } from 'svelte-spa-router'
import { pageStore } from '../lib/store'
import moment from 'moment/min/moment-with-locales'
moment.locale('ko')


let job_list = []

let pageValue;

pageStore.subscribe((value) => {
    console.log(value);
    pageValue = value;
});


let size = 30
let total = 0
$: total_page = Math.ceil(total/size)

function get_job_list(_page) {
    let params = {
        page: _page,
        size: size,
    }
    fastapi('get', '/api/job/list', params, (json) => {
        job_list = json.job_list
        pageValue = _page
        total = json.total
    })
}

get_job_list(pageValue)

</script>

<div class="container my-3">
    <table class="table">
        <tbody>
        {#each job_list as job, i}
        <tr>
            <td style="color:#929292" class="col-md-1 text-center">{moment(job.create_date).format("MM/DD")}</td>
            <td>
                <a use:link href="/detail/{job.id}/{pageValue}">
                    <span style="color:#171717">{job.subject}</span>
                    <span style="font-size:10pt; color:#6a6a6a; margin-left:50px;">{job.sido} > {job.gugun}</span>
                </a>
            </td>
        </tr>
        {/each}
        </tbody>
    </table>

    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {pageValue <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_job_list(pageValue-1)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
            {#if loop_page >= pageValue-4 && loop_page <= pageValue+4} 
            <li class="page-item {loop_page === pageValue && 'active'}">
                <button on:click="{() => get_job_list(loop_page)}" class="page-link">{loop_page+1}</button>
            </li>
            {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {pageValue >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_job_list(pageValue+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
                
</div>

