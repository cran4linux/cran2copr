%global __brp_check_rpaths %{nil}
%global packname  bcv
%global packver   1.0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation for the SVD (Bi-Cross-Validation)

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Methods for choosing the rank of an SVD approximation via cross
validation.  The package provides both Gabriel-style "block" holdouts and
Wold-style "speckled" holdouts.  It also includes an implementation of the
SVDImpute algorithm.  For more information about Bi-cross-validation, see
Owen & Perry's 2009 AoAS article (at <arXiv:0908.2062>) and Perry's 2009
PhD thesis (at <arXiv:0909.3052>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
