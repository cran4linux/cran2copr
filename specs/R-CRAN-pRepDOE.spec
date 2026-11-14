%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pRepDOE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construction of p-Rep Designs from Graph and Finite-Field Structures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Constructs partially replicated (p-rep) designs in which every treatment
occurs in every location, once or twice in Methods I and III and q or q +
1 times in Method II, with constant overall replication. Method I
decomposes the complete graph into Hamiltonian paths, Method II uses
cyclic blocks derived from a Hamiltonian cycle, and Method III uses
mutually orthogonal Latin squares over a Galois field. Three
treatment-replacement extensions (block enlargement, block splitting, and
replacement followed by column-wise splitting) can be applied to Methods I
and II. Each design is checked for connectedness and is returned with its
parameters, pairwise concurrence distribution, canonical efficiency factor
(CEF), average variance factor (AVF) and a randomized layout. Background
references: Vinaykumar et al. (2026) <doi:10.1007/s12355-025-01684-1>;
Vinaykumar et al. (2024) <doi:10.1080/03610926.2023.2185753>; Williams et
al. (2011) <doi:10.1002/bimj.201000102>.

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
