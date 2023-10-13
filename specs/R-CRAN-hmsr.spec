%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmsr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multipopulation Evolutionary Strategy HMS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-graphics 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-msm 
Requires:         R-methods 
Requires:         R-CRAN-uuid 
Requires:         R-graphics 

%description
The HMS (Hierarchic Memetic Strategy) is a composite global optimization
strategy consisting of a multi-population evolutionary strategy and some
auxiliary methods. The HMS makes use of a dynamically-evolving data
structure that provides an organization among the component populations.
It is a tree with a fixed maximal height and variable internal node
degree. Each component population is governed by a particular evolutionary
engine. This package provides a simple R implementation with examples of
using different genetic algorithms as the population engines. References:
J. Sawicki, M. Łoś, M. Smołka, J. Alvarez-Aramberri (2022)
<doi:10.1007/s11047-020-09836-w>.

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
