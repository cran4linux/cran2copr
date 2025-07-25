%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BrokenAdaptiveRidge
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Broken Adaptive Ridge Regression with Cyclops

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Cyclops >= 3.0.0
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-bit64 
Requires:         R-CRAN-Cyclops >= 3.0.0
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-bit64 

%description
Approximates best-subset selection (L0) regression with an iteratively
adaptive Ridge (L2) penalty for large-scale models. This package uses
Cyclops for an efficient implementation and the iterative method is
described in Kawaguchi et al (2020) <doi:10.1002/sim.8438> and Li et al
(2021) <doi:10.1016/j.jspi.2020.12.001>.

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
