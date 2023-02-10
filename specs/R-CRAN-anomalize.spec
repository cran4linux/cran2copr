%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  anomalize
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Anomaly Detection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tibbletime >= 0.1.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-sweep 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tibbletime >= 0.1.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-sweep 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-rstudioapi 

%description
The 'anomalize' package enables a "tidy" workflow for detecting anomalies
in data. The main functions are time_decompose(), anomalize(), and
time_recompose(). When combined, it's quite simple to decompose time
series, detect anomalies, and create bands separating the "normal" data
from the anomalous data at scale (i.e. for multiple time series). Time
series decomposition is used to remove trend and seasonal components via
the time_decompose() function and methods include seasonal decomposition
of time series by Loess ("stl") and seasonal decomposition by piecewise
medians ("twitter"). The anomalize() function implements two methods for
anomaly detection of residuals including using an inner quartile range
("iqr") and generalized extreme studentized deviation ("gesd"). These
methods are based on those used in the 'forecast' package and the Twitter
'AnomalyDetection' package. Refer to the associated functions for specific
references for these methods.

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
