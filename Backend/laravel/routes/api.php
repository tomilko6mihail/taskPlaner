<?php

use App\Http\Controllers\Api\TaskController;
use App\Http\Controllers\Auth\AuthController;
use App\Http\Controllers\tasks;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');


Route::get('/tasks', [TaskController::class, 'sendTasks']);
Route::get('/tasks/{id}', [TaskController::class, 'id']);
Route::post('/login', [AuthController:: class, 'login']);