%global __brp_check_rpaths %{nil}
%global packname  itp
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Interpolate, Truncate, Project (ITP) Root-Finding Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Rcpp >= 1.0.8

%description
Implements the Interpolate, Truncate, Project (ITP) root-finding algorithm
developed by Oliveira and Takahashi (2021) <doi:10.1145/3423597>. The user
provides the function, from the real numbers to the real numbers, and an
interval with the property that the values of the function at its
endpoints have different signs. If the function is continuous over this
interval then the ITP method estimates the value at which the function is
equal to zero. If the function is discontinuous then a point of
discontinuity at which the function changes sign may be found. The
function can be supplied using either an R function or an external pointer
to a C++ function. Tuning parameters of the ITP algorithm can be set by
the user. Default values are set based on arguments in Oliveira and
Takahashi (2021).

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
