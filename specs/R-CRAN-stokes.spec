%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stokes
%global packver   1.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Exterior Calculus

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-permutations >= 1.1.2
BuildRequires:    R-CRAN-spray >= 1.0.26
BuildRequires:    R-CRAN-disordR >= 0.9.7
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-methods 
Requires:         R-CRAN-permutations >= 1.1.2
Requires:         R-CRAN-spray >= 1.0.26
Requires:         R-CRAN-disordR >= 0.9.7
Requires:         R-CRAN-partitions 
Requires:         R-methods 

%description
Provides functionality for working with tensors, alternating forms, wedge
products, Stokes's theorem, and related concepts from the exterior
calculus.  Uses 'disordR' discipline (Hankin, 2022,
<doi:10.48550/arXiv.2210.03856>).  The canonical reference would be M.
Spivak (1965, ISBN:0-8053-9021-9) "Calculus on Manifolds".  To cite the
package in publications please use Hankin (2022)
<doi:10.48550/arXiv.2210.17008>.

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
