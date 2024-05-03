%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BMconcor
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          CONCOR for Structural- And Regular-Equivalence Blockmodeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The four functions svdcp() ('cp' for column partitioned), svdbip() or
svdbip2() ('bip' for bipartitioned), and svdbips() ('s' for a simultaneous
optimization of a set of 'r' solutions), correspond to a singular value
decomposition (SVD) by blocks notion, by supposing each block depending on
relative subspaces, rather than on two whole spaces as usual SVD does. The
other functions, based on this notion, are relative to two column
partitioned data matrices x and y defining two sets of subsets x_i and y_j
of variables and amount to estimate a link between x_i and y_j for the
pair (x_i, y_j) relatively to the links associated to all the other pairs.
These methods were first presented in: Lafosse R. & Hanafi M.,(1997)
<https://eudml.org/doc/106424> and Hanafi M. & Lafosse, R. (2001)
<https://eudml.org/doc/106494>.

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
