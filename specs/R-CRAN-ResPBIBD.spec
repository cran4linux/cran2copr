%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ResPBIBD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          "Resolvable Partially Balanced Incomplete Block Designs (PBIBDs)"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of several utility functions related to resolvable and affine
resolvable Partially Balanced Incomplete Block Designs (PBIBDs), have been
developed. In the class of resolvable designs, affine resolvable designs
are said to be optimal, Bailey (1995) <doi:10.2307/2337638>. Here, the
package contains three functions to generate and study the
characterization properties of these designs. Developed functions are
named as PBIBD1(), PBIBD2() and PBIBD3(), in which first two functions are
used to generate two new series of affine resolvable PBIBDs and last one
is used to generate a new series of resolvable PBIBDs, respectively.  In
addition, these functions can also be used to generate design parameters
(v, b, r and k), canonical efficiency factors, variance factor between
associates and average variance factors of the generated designs. Here v
is the number of treatments, b (= b1 + b2, in case of non-proper design)
is the number of blocks, r is the number of replications and k (= k1 + k2;
k1 is the size of b1 and k2 is the size of b2) is the block size.

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
