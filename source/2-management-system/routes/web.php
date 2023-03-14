<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PageController;
use App\Http\Controllers\AuthenticationController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [PageController::class, 'ViewIndexPageFunction'])->name("IndexPageLink");

Route::post('/login-function', [AuthenticationController::class, 'LoginFunction'])->name("LoginFunctionLink");

Route::get('/logout-function', [AuthenticationController::class, 'LogoutFunction'])->name("LogoutFunctionLink");

Route::get('/home-page-view', [PageController::class, 'ViewHomePageFunction'])->name("HomePageViewLink");

Route::get('/vision-data-view', [PageController::class, 'ViewVisionDataFunction'])->name("VisionDataViewLink");

Route::get('/audio-data-view', [PageController::class, 'ViewAudioDataFunction'])->name("AudioDataViewLink");