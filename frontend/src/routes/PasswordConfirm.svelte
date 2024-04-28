<script>
    import { push } from 'svelte-spa-router'
    import { link } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    export let params = {}
    let error = {detail:[]}
    let job_id = params.job_id
    let page = params.page
    let password = ''
    function password_confirm(event) {
        event.preventDefault()
        let url = "/api/member/password_confirm"
        let params = {
            job_id: job_id,
            password: password,
        }
        fastapi('post', url, params,
            (json) => {
                if (json == false) {
                    alert("비밀번호가 틀립니다.")
                    return false;
                }
                push("/job-modify/"+job_id+"/"+page)
            },
            (json_error) => {
                error = json_error
            }
        )
    }


</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">비밀번호 확인</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="password">비밀번호 입력</label>
            <input type="text" class="form-control" bind:value="{password}">
        </div>

        <a href={`/`} use:link class="btn btn-primary">뒤로</a>
        <button class="btn btn-primary" on:click="{password_confirm}" style="width:200px;margin-left:100px;">확인</button>

    </form>
</div>