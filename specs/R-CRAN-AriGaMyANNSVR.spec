%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AriGaMyANNSVR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid ARIMA-GARCH and Two Specially Designed ML-Based Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AllMetrics 
BuildRequires:    R-CRAN-DescribeDF 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-FinTS 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-aTSA 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-AllMetrics 
Requires:         R-CRAN-DescribeDF 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-FinTS 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-aTSA 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-e1071 

%description
Describes a series first. After that does time series analysis using one
hybrid model and two specially structured Machine Learning (ML)
(Artificial Neural Network or ANN and Support Vector Regression or SVR)
models. More information can be obtained from Paul and Garai (2022)
<doi:10.1007/s41096-022-00128-3>.

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
