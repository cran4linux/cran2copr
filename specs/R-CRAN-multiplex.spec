%global __brp_check_rpaths %{nil}
%global packname  multiplex
%global packver   2.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Algebraic Tools for the Analysis of Multiple Social Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Algebraic procedures for the analysis of multiple social networks are
delivered with this package as described in Ostoic (2020)
<DOI:10.18637/jss.v092.i11>. Among other things, it makes it possible to
create and manipulate multiplex, multimode, and multilevel network data
with different formats. There are effective ways available to treat
multiple networks with routines that combine algebraic systems like the
partially ordered semigroup or the semiring structure with the relational
bundles occurring in different types of multivariate network data sets. It
also provides an algebraic approach for affiliation networks through
Galois derivations between families of the pairs of subsets in the two
domains.

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
