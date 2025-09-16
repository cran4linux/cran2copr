%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waou
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighting All of Us

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-nonprobsvy 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-nonprobsvy 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 

%description
Utilities for using a probability sample to reweight prevalence estimates
calculated from the All of Us research program. Weighted estimates will
still not be representative of the general U.S. population. However, they
will provide an early indication for how unweighted estimates may be
biased by the sampling bias in the All of Us sample.

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
