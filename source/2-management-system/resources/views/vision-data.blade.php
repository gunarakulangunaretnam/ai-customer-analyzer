@extends('dashboard-layout.base-template')

@section('content')

<div class="container-fluid">

    <!-- Page Heading -->

    <div class="jumbotron">
        <div class="row">
            <div class="col-md-3 offset-md-3 col-lg-3 offset-lg-4">
                <div class="input-group input-group-sm mb-3">
                    <div class="input-group-prepend">
                        <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Search by Date:</span>
                    </div>
                    <input type="date" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm">
                </div>
            </div>
        </div>
    </div>
    
    <div class="row">

        <table style="background-color: white; border: 5px solid rgb(197, 189, 189);" class="table table-hover table-light">
            <thead style="color:balck; background-color: #e3e5e8;">
              <tr>
                <th scope="col">No</th>
                <th scope="col">Date</th>
                <th scope="col">Time</th>
                <th scope="col">Image</th>
                <th scope="col">Mask</th>
                <th scope="col">Age</th>
                <th scope="col">Gender</th>
                <th scope="col">Emotion</th>
                <th scope="col">Race</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>

              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>

              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>

              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>

              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>

              <tr>
                <th scope="row">1</th>
                <td>2023-03-11</td>
                <td>14:01:32</td>
                <td>

                    <div class="card" style="width: 18rem;">
                        <a target="_blank" href="https://www.gstatic.com/webp/gallery/1.jpg"><img class="card-img-top" src="https://www.gstatic.com/webp/gallery/1.jpg" alt="Card image cap"></a>
                      </div>

                </td>
                <td>Not Found</td>
                <td>28</td>
                <td>Male</td>
                <td>Happy</td>
                <td>Asian</td>
              </tr>
             
            </tbody>
          </table>

    </div>
        
</div>

@endsection