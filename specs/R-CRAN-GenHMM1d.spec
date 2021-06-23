%global __brp_check_rpaths %{nil}
%global packname  GenHMM1d
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit for Univariate Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-ssdtools 
BuildRequires:    R-CRAN-VaRES 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixcalc 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-ssdtools 
Requires:         R-CRAN-VaRES 
Requires:         R-CRAN-VGAM 

%description
Inference, goodness-of-fit tests, and predictions for continuous and
discrete univariate Hidden Markov Models (HMM). The goodness-of-fit test
is based on a Cramer-von Mises statistic and uses parametric bootstrap to
estimate the p-value. The description of the methodology is taken from
Nasri et al (2020) <doi:10.1029/2019WR025122>.

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
