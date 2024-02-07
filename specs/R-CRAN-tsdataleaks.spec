%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsdataleaks
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exploit Data Leakages in Time Series Forecasting Competitions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-stats 
Requires:         R-CRAN-slider 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-viridis 

%description
Forecasting competitions are of increasing importance as a mean to learn
best practices and gain knowledge. Data leakage is one of the most common
issues that can often be found in competitions. Data leaks can happen when
the training data contains information about the test data. For example:
randomly chosen blocks of time series are concatenated to form a new time
series, scale-shifts, repeating patterns in time series, white noise is
added in the original time series to form a new time series, etc.
'tsdataleaks' package can be used to detect data leakages in a collection
of time series.

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
