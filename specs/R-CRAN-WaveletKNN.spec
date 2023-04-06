%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaveletKNN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Based K-Nearest Neighbor Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caretForecast 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavelets 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caretForecast 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-tseries 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 

%description
The employment of the Wavelet decomposition technique proves to be highly
advantageous in the modelling of noisy time series data. Wavelet
decomposition technique using the "haar" algorithm has been incorporated
to formulate a hybrid Wavelet KNN (K-Nearest Neighbour) model for time
series forecasting, as proposed by Anjoy and Paul (2017)
<DOI:10.1007/s00521-017-3289-9>.

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
