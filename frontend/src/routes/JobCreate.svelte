<script>
    import { push } from 'svelte-spa-router'
    import { link } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let subject = ''
    let password = ''
    let content = ''
    let selectedSido = ''
    let selectedGugun = ''
    let sidos = []
    let guguns = []

    function post_job(event) {
        event.preventDefault()
        let url = "/api/job/create"
            let params = {
            sido: selectedSido,
            gugun: selectedGugun,
            subject: subject,
            content: content,
            password: password,
        }
        fastapi('post', url, params,
            (json) => {
                push("/")
            },
            (json_error) => {
                error = json_error
            }
        )
    }


    function change_sido() {

        let url = "/api/job/city_data"
        fastapi('get', url,{"sido_name":selectedSido},
            (json) => {
                sidos = json.sido
                guguns = json.gugun

                selectedGugun = ''

            },
            (json_error) => {
                error = json_error
            }
        )
    }

    change_sido()

</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">구인 등록</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="row align-items-center mb-3">
            <div class="col-sm-12 col-md-2"><label for="subject">지역</label></div>
            <div class="col-sm-12 col-md-4">
                <select class="form-select" aria-label="Default select example" bind:value={selectedSido} on:change={change_sido}>
                    <option value="">시/도</option>
                    {#each sidos as sido}
                        <option value={sido}>{sido}</option>
                    {/each}
                </select>
            </div>
            <div class="col-sm-12 col-md-4">
                <select class="form-select" aria-label="Default select example" bind:value={selectedGugun}>
                    <option value="">시/군/구</option>
                    {#each guguns as gugun}
                        <option value={gugun}>{gugun}</option>
                    {/each}
                </select>
            </div>
        </div>
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" class="form-control" bind:value="{subject}">
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{content}"></textarea>
        </div>
        <div class="mb-3">
            <label for="subject">비밀번호</label>
            <input type="text" class="form-control" bind:value="{password}">
        </div>

        <div class="row start align-items-center justify-content-center mt-3">
            <div class="col-auto"><a href={`/`} use:link class="btn btn-primary">뒤로</a></div>
            <div class="col-auto"><button class="btn btn-primary" on:click="{post_job}">등록하기</button></div>
        </div>
    </form>
</div>


