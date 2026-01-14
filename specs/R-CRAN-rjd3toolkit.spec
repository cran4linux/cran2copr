%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3toolkit
%global packver   3.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions Around 'JDemetra+ 3.0'

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 1.0.6
BuildRequires:    R-CRAN-RProtoBuf >= 0.4.20
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjd3jars 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rJava >= 1.0.6
Requires:         R-CRAN-RProtoBuf >= 0.4.20
Requires:         R-CRAN-checkmate 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rjd3jars 
Requires:         R-stats 
Requires:         R-utils 

%description
R Interface to 'JDemetra+ 3.x' (<https://github.com/jdemetra>) time series
analysis software.  It provides functions allowing to model time series
(create outlier regressors, user-defined calendar regressors, Unobserved
Components AutoRegressive Integrated Moving Average (UCARIMA) models...),
to test the presence of trading days or seasonal effects and also to set
specifications in pre-adjustment and benchmarking when using 'rjd3x13' or
'rjd3tramoseats'.

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
