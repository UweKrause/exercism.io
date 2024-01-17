use std::ops::Rem;

struct Year {
    year: u64,
}

impl Year {
    pub fn is_leap_year(&self) -> bool {
        self.is_evenly_divisible(4)
            & !(
            self.is_evenly_divisible(100)
                & !self.is_evenly_divisible(400)
        )
    }

    fn is_evenly_divisible(&self, by: u64) -> bool {
        self.year.rem(by) == 0
    }
}


pub fn is_leap_year(year: u64) -> bool {
    Year { year }.is_leap_year()
}
