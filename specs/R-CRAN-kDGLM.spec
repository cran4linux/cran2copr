%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kDGLM
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Dynamic Generalized Linear Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast >= 2.0.8
BuildRequires:    R-CRAN-extraDistr >= 1.9.1
BuildRequires:    R-CRAN-generics >= 0.1.3
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rfast >= 2.0.8
Requires:         R-CRAN-extraDistr >= 1.9.1
Requires:         R-CRAN-generics >= 0.1.3
Requires:         R-CRAN-Rdpack 

%description
Provide routines for filtering and smoothing, forecasting, sampling and
Bayesian analysis of Dynamic Generalized Linear Models using the
methodology described in Alves et al.
(2024)<doi:10.48550/arXiv.2201.05387> and dos Santos Jr. et al.
(2024)<doi:10.48550/arXiv.2403.13069>.

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
