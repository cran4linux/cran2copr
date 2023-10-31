%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  anomaly
%global packver   4.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting Anomalies in Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-cowplot 

%description
Implements Collective And Point Anomaly (CAPA) Fisch, Eckley, and
Fearnhead (2022) <doi:10.1002/sam.11586>, Multi-Variate Collective And
Point Anomaly (MVCAPA) Fisch, Eckley, and Fearnhead (2021)
<doi:10.1080/10618600.2021.1987257>, Proportion Adaptive Segment Selection
(PASS) Jeng, Cai, and Li (2012) <doi:10.1093/biomet/ass059>, and Bayesian
Abnormal Region Detector (BARD) Bardwell and Fearnhead (2015)
<arXiv:1412.5565>. These methods are for the detection of anomalies in
time series data.

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
