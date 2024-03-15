%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiSCos
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Distributional Synthetic Controls Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-evmix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-extremeStat 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-evmix 
Requires:         R-utils 
Requires:         R-CRAN-extremeStat 
Requires:         R-CRAN-MASS 

%description
The method of synthetic controls is a widely-adopted tool for evaluating
causal effects of policy changes in settings with observational data. In
many settings where it is applicable, researchers want to identify causal
effects of policy changes on a treated unit at an aggregate level while
having access to data at a finer granularity. This package implements a
simple extension of the synthetic controls estimator, developed in
Gunsilius (2023) <doi:10.3982/ECTA18260>, that takes advantage of this
additional structure and provides nonparametric estimates of the
heterogeneity within the aggregate unit. The idea is to replicate the
quantile function associated with the treated unit by a weighted average
of quantile functions of the control units. The package contains tools for
aggregating and plotting the resulting distributional estimates, as well
as for carrying out inference on them.

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
