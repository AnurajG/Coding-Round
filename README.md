# Coding-Round

### <a name="spark">Spark</a>
Using the two datasets voltage and current calculate the power consumed. Please note that we need to upsample Current to match the frequency of Voltage recordings.
```
Power(t)=Current(t)*Volatge(t)
```

The output shall look like below

| Time | Voltage  |  Current |   Power    |  
| ---- | -------- | -------- | ---------- |
|0	   | 121      |  774	 |  93654     | 
|0.01  | 23	      |  774	 |  17802     |
|0.02  | 136	  |  774	 |  105264    |
|0.03  | 15	      |  774	 |  11610     |
|0.04  | 155	  |  774	 |  119970    |
|0.05  | 66	      |  774	 |  51084     |
|0.06  | 215	  |  774	 |  166410    |
|0.07  | 98	      |  774	 |  75852     |
|0.08  | 131	  |  774	 |  101394    |
|0.09  | 148	  |  774	 |  114552    |
|0.1   | 182	  |  444	 |  80808     |
|0.11  | 196	  |  444	 |  87024     |
|0.12  | 80	      |  444	 |  35520     |

...

### <a name="kube">Kubernetes</a>
Write an SQL query to calculate the MAX Power every 1/10th of second (0.1).
| Time |   Power    |  
| ---- | ---------- |
|0	   |  166410    | 
|0.1   |  89688     |
...

### <a name="kube">Kubernetes</a>
Create a Pod with two containers, both with image busybox and command "echo hello; sleep 3600". Connect to the second container and run 'ls'
