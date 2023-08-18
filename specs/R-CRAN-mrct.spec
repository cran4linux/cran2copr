%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mrct
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection of Functional Data Based on the Minimum Regularized Covariance Trace Estimator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fdapace 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Detect outlying observations in functional data sets based on the minimum
regularized covariance trace (MRCT) estimator. Includes implementation of
Oguamalam et al. (2023) <arXiv:2307.13509>.

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
