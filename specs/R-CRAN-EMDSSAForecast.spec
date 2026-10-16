%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMDSSAForecast
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid EMD-SSA Forecasting with Artificial Neural Networks for Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rlibeemd 
BuildRequires:    R-CRAN-Rssa 
BuildRequires:    R-CRAN-neuralnet 
Requires:         R-CRAN-Rlibeemd 
Requires:         R-CRAN-Rssa 
Requires:         R-CRAN-neuralnet 

%description
Implements a hybrid empirical mode decomposition, singular spectrum
analysis, and artificial neural network forecasting framework for time
series data. The framework extracts the trend from the first intrinsic
mode function using singular spectrum analysis, forecasts the extracted
trend and remaining decomposition components using artificial neural
networks, and combines the component forecasts to obtain the final
forecast. For methodological details, refer to Kumar et al. (2026)
<doi:10.1007/s10791-026-10076-2>.

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
