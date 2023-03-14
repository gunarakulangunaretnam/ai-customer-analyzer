@extends('dashboard-layout.base-template')
@section('content')

    <!-- Begin Page Content -->
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

            <table style="background-color: white; border: 5px solid rgb(197, 189, 189); table-layout: fixed;" class="table table-hover table-light">
                <thead style="color:balck; background-color: #e3e5e8;">
                    <tr>
                    <th style="width: 60px;" scope="col">No</th>
                    <th scope="col">Date</th>
                    <th scope="col">Time</th>
                    <th scope="col">Stall No</th>
                    <th scope="col">Employee ID</th>
                    <th scope="col">Employee Name</th>
                    <th style="width: 350px;" scope="col">Transcription</th>
                    <th scope="col">Prediction</th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                    <th scope="row">1</th>
                    <td>2023-03-11</td>
                    <td>14:01:32</td>
                    <td>S-132</td>
                    <td>E-18</td>
                    <td>David Juthushan</td>
                    <td style="text-align: justify;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                        molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                        numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                        optio, eaque rerum! Provident similique accusantium nemo autem.
                        </td>
                    <td style="font-weight: bold; color:blue;">Positive</td>
                    </tr>

                    <tr>
                    <th scope="row">1</th>
                    <td>2023-03-11</td>
                    <td>14:01:32</td>
                    <td>S-132</td>
                    <td>E-18</td>
                    <td>David Juthushan</td>
                    <td style="text-align: justify;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                        molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                        numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                        optio, eaque rerum! Provident similique accusantium nemo autem.
                        </td>
                    <td style="font-weight: bold; color:red;">Negative</td>
                    </tr>

                    <tr>
                    <th scope="row">1</th>
                    <td>2023-03-11</td>
                    <td>14:01:32</td>
                    <td>S-132</td>
                    <td>E-18</td>
                    <td>David Juthushan</td>
                    <td style="text-align: justify;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                        molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                        numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                        optio, eaque rerum! Provident similique accusantium nemo autem.
                        </td>
                    <td style="font-weight: bold; color:blue;">Positive</td>
                    </tr>

                    <tr>
                    <th scope="row">1</th>
                    <td>2023-03-11</td>
                    <td>14:01:32</td>
                    <td>S-132</td>
                    <td>E-18</td>
                    <td>David Juthushan</td>
                    <td style="text-align: justify;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                        molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                        numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                        optio, eaque rerum! Provident similique accusantium nemo autem.
                        </td>
                    <td style="font-weight: bold; color:red;">Negative</td>
                    </tr>

                    <tr>
                    <th scope="row">1</th>
                    <td>2023-03-11</td>
                    <td>14:01:32</td>
                    <td>S-132</td>
                    <td>E-18</td>
                    <td>David Juthushan</td>
                    <td style="text-align: justify;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                        molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                        numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                        optio, eaque rerum! Provident similique accusantium nemo autem.
                        </td>
                    <td style="font-weight: bold; color:blue;">Positive</td>
                    </tr>

                    
                </tbody>
                </table>

        </div>
            
    </div>


@endsection
