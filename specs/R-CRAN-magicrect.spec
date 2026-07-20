%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  magicrect
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Magic Rectangles and Nearly Magic Rectangles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Constructs a magic rectangle or a nearly magic rectangle of order p x q
for every order for which one exists, together with existence
classification and verification utilities. A magic rectangle arranges the
integers 1 to p*q so that all row sums are equal and all column sums are
equal; it exists exactly when p and q have the same parity, excluding 2 x
2 and degenerate single-row/column cases (Hagedorn, 1999,
<doi:10.1016/S0012-365X(99)00041-2>). When p and q have opposite parity a
nearly magic rectangle exists instead, with constant sums along one
direction and sums differing by at most one along the other (Chai, Singh
and Stufken, 2019, Journal of Combinatorial Designs 27(6), 368-376).
Implements the constructions of De Los Reyes, Das, Midha and Vellaisamy
(2009) for even by even orders, Chai, Das and Midha (2013) for odd by odd
orders, and Chai, Singh and Stufken (2019) for the nearly magic (even by
odd) case.

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
