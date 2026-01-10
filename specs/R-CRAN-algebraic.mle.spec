%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  algebraic.mle
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algebraic Maximum Likelihood Estimators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-algebraic.dist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-algebraic.dist 
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 

%description
Defines an algebra over maximum likelihood estimators (MLEs) by providing
operators that are closed over MLEs, along with various statistical
functions for inference. For background on maximum likelihood estimation,
see Casella and Berger (2002, ISBN:978-0534243128). For the delta method
and variance estimation, see Lehmann and Casella (1998,
ISBN:978-0387985022).

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
