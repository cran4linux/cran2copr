%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sense
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Stacked Ensemble for Regression Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-visNetwork >= 2.0.9
BuildRequires:    R-CRAN-readr >= 2.0.1
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-tictoc >= 1.0.1
BuildRequires:    R-CRAN-paradox >= 1.0.0
BuildRequires:    R-CRAN-mlr3tuning >= 0.8.0
BuildRequires:    R-CRAN-mlr3viz >= 0.5.5
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-mlr3learners >= 0.5.0
BuildRequires:    R-CRAN-mlr3filters >= 0.4.2
BuildRequires:    R-CRAN-mlr3pipelines >= 0.3.5.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-bbotk >= 0.3.2
BuildRequires:    R-CRAN-mlr3 >= 0.12.0
BuildRequires:    R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-visNetwork >= 2.0.9
Requires:         R-CRAN-readr >= 2.0.1
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-tictoc >= 1.0.1
Requires:         R-CRAN-paradox >= 1.0.0
Requires:         R-CRAN-mlr3tuning >= 0.8.0
Requires:         R-CRAN-mlr3viz >= 0.5.5
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-mlr3learners >= 0.5.0
Requires:         R-CRAN-mlr3filters >= 0.4.2
Requires:         R-CRAN-mlr3pipelines >= 0.3.5.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-bbotk >= 0.3.2
Requires:         R-CRAN-mlr3 >= 0.12.0
Requires:         R-CRAN-Metrics >= 0.1.4

%description
Stacked ensemble for regression tasks based on 'mlr3' framework with a
pipeline for preprocessing numeric and factor features and hyper-parameter
tuning using grid or random search.

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
