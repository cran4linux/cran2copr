%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dendrometry
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Estimations and Dendrometric Computations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Computation of dendrometric and structural parameters from forest
inventory data. The objective is to provide an user-friendly R package for
researchers, ecologists, foresters, statisticians, loggers and others
persons who deal with forest inventory data. Useful conversion of angle
value from degree to radian, conversion from angle to slope (in
percentage) and their reciprocals as well as principal angle determination
are also included. Position and dispersion parameters usually found in
forest studies are implemented. The package contains Fibonacci series, its
extensions and the Golden Number computation. Useful references are
Arcadius Y. J. Akossou, Soufianou Arzouma, Eloi Y. Attakpa, Noël H. Fonton
and Kouami Kokou (2013) <doi:10.3390/d5010099> and W. Bonou, R. Glele
Kakaï, A.E. Assogbadjo, H.N. Fonton, B. Sinsin (2009)
<doi:10.1016/j.foreco.2009.05.032> .

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
