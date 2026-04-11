%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scip
%global packver   1.10.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the SCIP Optimization Suite

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Provides an R interface to SCIP (Solving Constraint Integer Programs), a
framework for mixed-integer programming (MIP), mixed-integer nonlinear
programming (MINLP), and constraint integer programming (2025,
<doi:10.48550/arXiv.2511.18580>). Supports linear, quadratic, SOS,
indicator, and knapsack constraints with continuous, binary, and integer
variables. Includes a one-shot solver interface and a model-building API
for incremental problem construction.

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
