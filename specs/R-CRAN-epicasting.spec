%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epicasting
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ewnet: An Ensemble Wavelet Neural Network for Forecasting and Epicasting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavelets 
Requires:         R-datasets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-Metrics 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 

%description
Method and tool for generating time series forecasts using an ensemble
wavelet-based auto-regressive neural network architecture. This method
provides additional support of exogenous variables and also generates
confidence interval. This package provides EWNet model for time series
forecasting based on the algorithm by Panja, et al. (2022) and Panja, et
al. (2023) <arXiv:2206.10696> <doi:10.1016/j.chaos.2023.113124>.

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
