%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3forecast
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extending 'mlr3' to Time Series Forecasting

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-mlr3 >= 1.7.0
BuildRequires:    R-CRAN-backports >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.18.0
BuildRequires:    R-CRAN-paradox >= 1.0.1
BuildRequires:    R-CRAN-mlr3misc >= 0.22.0
BuildRequires:    R-CRAN-mlr3pipelines >= 0.11.0
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-mlr3 >= 1.7.0
Requires:         R-CRAN-backports >= 1.5.0
Requires:         R-CRAN-data.table >= 1.18.0
Requires:         R-CRAN-paradox >= 1.0.1
Requires:         R-CRAN-mlr3misc >= 0.22.0
Requires:         R-CRAN-mlr3pipelines >= 0.11.0
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-cli 
Requires:         R-CRAN-lgr 
Requires:         R-stats 
Requires:         R-utils 

%description
Extends the 'mlr3' package and ecosystem to time series forecasting.
Provides forecasting tasks, learners, resampling strategies, performance
measures, and 'mlr3pipelines' operators for time-series feature
engineering. Machine learning regression learners can be turned into
forecasters through recursive and direct multi-step strategies.

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
