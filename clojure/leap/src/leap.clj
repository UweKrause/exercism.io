(ns leap)

(defn even-divisable? [year divisor]
  (=(mod year divisor) 0)
)

(defn leap-year? [year]
  (and (even-divisable? year 4)
    (not
      (and
        (even-divisable? year 100)
        (not (even-divisable? year 400))
      )
    )
  )
)
