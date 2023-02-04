%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pbatR
%global packver   2.2-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.15
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree/Family-Based Genetic Association Tests Analysis and Power

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rootSolve 

%description
This R package provides power calculations via internal simulation
methods. The package also provides a frontend to the now abandoned PBAT
program (developed by Christoph Lange), and reads in the corresponding
output and displays results and figures when appropriate. The license of
this R package itself is GPL. However, to have the program interact with
the PBAT program for some functionality of the R package, users must
additionally obtain the PBAT program from Christoph Lange, and accept his
license. Both the data analysis and power calculations have command line
and graphical interfaces using tcltk.

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
