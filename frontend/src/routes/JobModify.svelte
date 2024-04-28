<script>
    import { push } from 'svelte-spa-router'
    import { link } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    export let params = {}
    const job_id = params.job_id
    const page = params.page

    let error = {detail:[]}
    let selectedSido = ''
    let selectedGugun = ''
    let subject = ''
    let content = ''
    let sidos = []
    let guguns = []


    let password = ''


    function modify_job(event) {
        event.preventDefault()
        let url = "/api/job/modify"
        let params = {
            job_id: job_id,
            sido: selectedSido,
            gugun: selectedGugun,
            subject: subject,
            content: content,
            password: password
        }
        fastapi('post', url, params,
            (json) => {
                push('/detail/'+job_id+'/'+page)
            },
            (json_error) => {
                error = json_error
            }
        )
    }


    function get_job(job_id) {
        return new Promise((resolve, reject) => {
            // 비동기 작업 수행
            fastapi("get", "/api/job/detail/" + job_id, {}, (json) => {
                resolve(json);
            })
        });
    }

    get_job(job_id).then((json) => {
        subject = json.subject
        content = json.content
        selectedSido = json.sido
        selectedGugun = json.gugun

        let url = "/api/job/city_data"
        fastapi('get', url,{"sido_name":selectedSido},
            (json) => {
                sidos = json.sido
                guguns = json.gugun
            },
            (json_error) => {
                error = json_error
            }
        )
    })

    function change_sido() {

        if (!selectedSido){
            selectedSido = ''
            selectedGugun = ''
            return false;
        }

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


</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2" style="color: dimgray;">구인 수정</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="row start align-items-center mb-3">
            <div class="col-3">
                <label for="password">비밀번호</label>
            </div>
            <div class="col-9">
                <input type="text" class="form-control" bind:value="{password}">
            </div>
        </div>

        <div class="row start align-items-center mb-3">
            <div class="col-3">
                <label for="subject">지역</label>
            </div>
            <div class="col-5">
                <select class="form-select" aria-label="Default select example" bind:value={selectedSido} on:change={change_sido}>
                    <option value="">시/도</option>
                  {#each sidos as sido}
                    <option value={sido}>{sido}</option>
                  {/each}
                </select>
            </div>
            <div class="col-4">
                <select class="form-select" aria-label="Default select example" bind:value={selectedGugun}>
                    <option value="">시/군/구</option>
                  {#each guguns as gugun}
                    <option value={gugun}>{gugun}</option>
                  {/each}
                </select>
            </div>
        </div>
        <div class="row start align-items-center mb-3">
            <div class="col-3"><label for="subject">제목</label></div>
            <div class="col-9"><input type="text" class="form-control" bind:value="{subject}"></div>
        </div>
        <div>
            <label class="mt-4 mb-2" for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{content}"></textarea>
        </div>
        <div class="row start align-items-center justify-content-center mt-3">
            <div class="col-auto"><a href={`/`} use:link class="btn btn-primary">취소</a></div>
            <div class="col-auto"><button class="btn btn-primary" on:click="{modify_job}">수정하기</button></div>
        </div>
    </form>
</div>
