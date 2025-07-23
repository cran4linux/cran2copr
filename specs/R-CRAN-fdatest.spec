%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdatest
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interval Testing Procedure for Functional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
Requires:         R-CRAN-fda 

%description
Implementation of the Interval Testing Procedure for functional data in
different frameworks (i.e., one or two-population frameworks, functional
linear models) by means of different basis expansions (i.e., B-spline,
Fourier, and phase-amplitude Fourier). The current version of the package
requires functional data evaluated on a uniform grid; it automatically
projects each function on a chosen functional basis; it performs the
entire family of multivariate tests; and, finally, it provides the matrix
of the p-values of the previous tests and the vector of the corrected
p-values. The functional basis, the coupled or uncoupled scenario, and the
kind of test can be chosen by the user. The package provides also a
plotting function creating a graphical output of the procedure: the
p-value heat-map, the plot of the corrected p-values, and the plot of the
functional data.

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
