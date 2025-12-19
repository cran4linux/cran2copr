%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tagtools
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Data from High-Resolution Biologging Tags

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-zoom 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-zoom 

%description
High-resolution movement-sensor tags typically include accelerometers to
measure body posture and sudden movements or changes in speed,
magnetometers to measure direction of travel, and pressure sensors to
measure dive depth in aquatic or marine animals. The sensors in these tags
usually sample many times per second. Some tags include sensors for speed,
turning rate (gyroscopes), and sound. This package provides software tools
to facilitate calibration, processing, and analysis of such data. Tools
are provided for: data import/export; calibration (from raw data to
calibrated data in scientific units); visualization (for example,
multi-panel time-series plots); data processing (such as event detection,
calculation of derived metrics like jerk and dynamic acceleration, dive
detection, and dive parameter calculation); and statistical analysis (for
example, track reconstruction, a rotation test, and Mahalanobis distance
analysis).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
