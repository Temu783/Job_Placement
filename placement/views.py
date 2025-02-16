from django.shortcuts import render
from .agents import predict_job

def predicted_job(request):
    features = ["ssc_percentage", "hsc_percentage", "degree_percentage",
                "mba_percent", "gender_M", "work_experience_Yes"]

    if request.method == 'POST':
        input_data = [float(request.POST[feature]) for feature in features]

        # Directly call predict_job
        result = predict_job(input_data)

        return render(request, 'prediction/result.html', {'result': result, 'features': zip(features, input_data)})

    return render(request, 'prediction/form.html', {'features': features})
