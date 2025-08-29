%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modeltime.ensemble
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Algorithms for Time Series Forecasting with Modeltime

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.5.0
BuildRequires:    R-CRAN-modeltime >= 1.2.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-modeltime.resample >= 0.2.1
BuildRequires:    R-CRAN-workflows >= 0.2.1
BuildRequires:    R-CRAN-tune >= 0.1.2
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-recipes >= 0.1.15
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-timetk >= 2.5.0
Requires:         R-CRAN-modeltime >= 1.2.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-modeltime.resample >= 0.2.1
Requires:         R-CRAN-workflows >= 0.2.1
Requires:         R-CRAN-tune >= 0.1.2
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-recipes >= 0.1.15
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tictoc 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 

%description
A 'modeltime' extension that implements time series ensemble forecasting
methods including model averaging, weighted averaging, and stacking. These
techniques are popular methods to improve forecast accuracy and stability.

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
