%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jordan
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Suite of Routines for Working with Jordan Algebras

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-onion >= 1.4.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quadform 
BuildRequires:    R-methods 
Requires:         R-CRAN-onion >= 1.4.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quadform 
Requires:         R-methods 

%description
A Jordan algebra is an algebraic object originally designed to study
observables in quantum mechanics.  Jordan algebras are commutative but
non-associative; they satisfy the Jordan identity.  The package follows
the ideas and notation of K. McCrimmon (2004, ISBN:0-387-95447-3) "A Taste
of Jordan Algebras".  To cite the package in publications, please use
Hankin (2023) <doi:10.48550/arXiv.2303.06062>.

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
