%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PGM2
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Construction of Nested Resolvable Designs and Associated Uniform Designs over GF(p)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Recursive construction of balanced incomplete block designs (BIBDs), their
successive generations, resolvable BIBDs (RBIBDs) and associated uniform
designs (UDs), derived from finite projective geometries PG(m, p) over a
Galois field GF(p) of any prime order p. Implements and generalises the
method of Boudraa, Gheribi-Aoulmi and Laib (2013, International Journal of
Research and Reviews in Applied Sciences, 17(2), 167-176), which was
previously available only for p = 2, and the uniform design constructions
of Fang et al. (2004) <doi:10.1016/S0012-365X(03)00100-6>. Designs of
every recursion stage can be extracted, and all constructions are
validated against the parameters published in the original paper.

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
