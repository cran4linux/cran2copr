%global packname  eye
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Eye Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-cli >= 2.2.0
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-lubridate >= 1.7.9.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-english >= 1.2.5
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-eyedata >= 0.1.0
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-cli >= 2.2.0
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-lubridate >= 1.7.9.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-english >= 1.2.5
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-eyedata >= 0.1.0

%description
There is no ophthalmic researcher who has not had headaches from the
handling of visual acuity entries. Different notations, untidy entries.
This shall now be a matter of the past. Eye makes it as easy as pie to
work with VA data - easy cleaning, easy conversion between Snellen,
logMAR, ETDRS letters, and qualitative visual acuity shall never pester
you again. The eye package automates the pesky task to count number of
patients and eyes, and can help to clean data with easy re-coding for
right and left eyes. It also contains functions to help reshaping eye side
specific variables between wide and long format. Visual acuity conversion
is based on Schulze-Bonsel et al. (2006) <doi:10.1167/iovs.05-0981>,
Gregori et al. (2010) <doi:10.1097/iae.0b013e3181d87e04>, Beck et al.
(2003) <doi:10.1016/s0002-9394(02)01825-1> and Bach (2007)
<http:michaelbach.de/sci/acuity.html>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
