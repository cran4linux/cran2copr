%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fingerprint
%global packver   3.5.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Operate on Binary Fingerprint Data

License:          GPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Functions to manipulate binary fingerprints of arbitrary length. A
fingerprint is represented by an object of S4 class 'fingerprint' which is
internally represented a vector of integers, such that each element
represents the position in the fingerprint that is set to 1. The bitwise
logical functions in R are overridden so that they can be used directly
with 'fingerprint' objects. A number of distance metrics are also
available (many contributed by Michael Fadock). Fingerprints can be
converted to Euclidean vectors (i.e., points on the unit hypersphere) and
can also be folded using OR.  Arbitrary fingerprint formats can be handled
via line handlers. Currently handlers are provided for CDK, MOE and BCI
fingerprint data.

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
