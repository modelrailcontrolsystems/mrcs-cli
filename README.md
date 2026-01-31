# mrcs-cli
_Command-line interface for the Model Rail Control Systems (MRCS) APIs_

---

### Repos

Requires MRCS repos:
* **[mrcs-core](https://github.com/modelrailcontrolsystems/mrcs-core)**

---

### Test sequence

Establish JWT session:
```
./mrcs_session -c
```

Set time, assert cron job, check time:
```
./mrcs_time -vi4 -vi4 -s -sr -ss 4 -sy 1930 -sm 1 -sd 2 -sh 6
./mrcs_publisher -vti4 -t CRN -n 3 -m '{"event_id": "abc", "on": "1930-01-02T06:02:00.104+00:00"}'
./mrcs_time -n
```
