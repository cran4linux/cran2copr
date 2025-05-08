%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clifford
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Arbitrary Dimensional Clifford Algebras

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-partitions >= 1.10.4
BuildRequires:    R-CRAN-freealg >= 1.0.4
BuildRequires:    R-CRAN-disordR >= 0.9.8.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-partitions >= 1.10.4
Requires:         R-CRAN-freealg >= 1.0.4
Requires:         R-CRAN-disordR >= 0.9.8.4
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
A suite of routines for Clifford algebras, using the 'Map' class of the
Standard Template Library.  Canonical reference: Hestenes (1987, ISBN
90-277-1673-0, "Clifford algebra to geometric calculus").  Special cases
including Lorentz transforms, quaternion multiplication, and Grassmann
algebra, are discussed. Vignettes presenting conformal geometric algebra,
quaternions and split quaternions, dual numbers, and Lorentz transforms
are included.  The package follows 'disordR' discipline.

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
