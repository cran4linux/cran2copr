%global packname  VLTimeCausality
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Variable-Lag Time Series Causality Inference Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-RTransferEntropy 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-RTransferEntropy 

%description
A framework to infer causality on a pair of time series of real numbers
based on variable-lag Granger causality and transfer entropy. Typically,
Granger causality and transfer entropy have an assumption of a fixed and
constant time delay between the cause and effect. However, for a
non-stationary time series, this assumption is not true. For example,
considering two time series of velocity of person A and person B where B
follows A. At some time, B stops tying his shoes, then running to catch up
A. The fixed-lag assumption is not true in this case. We propose a
framework that allows variable-lags between cause and effect in Granger
causality and transfer entropy to allow them to deal with variable-lag
non-stationary time series. Please see Chainarong Amornbunchornvej, Elena
Zheleva, and Tanya Berger-Wolf (2019) <arXiv:1912.10829> when referring to
this package in publications.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
