%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GETdesigns
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Extended Triangular Designs ('GETdesigns')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Since their introduction by Bose and Nair (1939)
<https://www.jstor.org/stable/40383923>, partially balanced incomplete
block (PBIB) designs remain an important class of incomplete block
designs. The concept of association scheme was used by Bose and Shimamoto
(1952) <doi:10.1080/01621459.1952.10501161> for the classification of
these designs. The constraint of resources always motivates the
experimenter to advance towards PBIB designs, more specifically to higher
associate class PBIB designs from balanced incomplete block designs. It is
interesting to note that many times higher associate PBIB designs perform
better than their counterpart lower associate PBIB designs for the same
set of parameters v, b, r, k and lambda_i (i=1,2...m). This package
contains functions named GETD() for generating m-associate (m>=2) class
PBIB designs along with parameters (v, b, r, k and lambda_i, i = 1, 2,…,m)
based on Generalized Triangular (GT) Association Scheme. It also
calculates the Information matrix, Average variance factor and canonical
efficiency factor of the generated design. These designs, besides having
good efficiency, require smaller number of replications and smallest
possible concurrence of treatment pairs.

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
