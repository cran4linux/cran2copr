%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baskwrap
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper Package for Several Basket Trial R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-basksim >= 0.1.0
BuildRequires:    R-CRAN-baskexact 
Requires:         R-CRAN-basksim >= 0.1.0
Requires:         R-CRAN-baskexact 

%description
A simple interface to switch between two methods for calculating basket
trial characteristics, numerical integration ("exact") and Monte Carlo
simulation ("simulated") for the basket trial design by Fujikawa et al.
2020 <doi:10.1002/bimj.201800404>. The exact implementation is from the
'baskexact' package, see Baumann (2024) <doi:10.1016/j.softx.2024.101793>.
The simulated implementation is from the 'basksim' package, which was
developed for Baumann et al. (2024) <doi:10.1080/19466315.2024.2402275>.
The package's syntax is compatible with the 'basksim' syntax and easily
extendable.

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
