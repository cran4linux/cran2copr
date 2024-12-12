%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TREDesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ternary Residual Effect Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
There are some experimental scenarios where each experimental unit
receives a sequence of treatments across multiple periods, and treatment
effects persist beyond the period of application. It focuses on the
construction and calculation of the parametric value of the residual
effect designs balanced for carryover effects, also referred to as
crossover designs, change-over designs, or repeated measurements designs
(Aggarwal and Jha, 2010<doi:10.1080/15598608.2010.10412013>). The primary
objective of the package is to generate a new class of Balanced Ternary
Residual Effect Designs (BTREDs), balanced for carryover effects tailored
explicitly for situations where the number of periods is less than or
equal to the number of treatments. In addition, the package provides four
new classes of Partially Balanced Ternary Residual Effect Designs
(PBTREDs), constructed using incomplete block designs, initial sequences,
and rectangular association scheme. In addition, one extra function is
included to help study the parametric properties of a given residual
effect design.

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
