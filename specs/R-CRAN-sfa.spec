%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sfa
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Frontier Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides a user-friendly framework for estimating a wide variety of
cross-sectional and panel stochastic frontier models. Suitable for a broad
range of applications, the implementation offers extensive flexibility in
specification and estimation techniques.

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
