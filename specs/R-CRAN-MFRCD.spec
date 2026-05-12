%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MFRCD
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Row-Column Designs for Asymmetrical Factorial Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Constructs and analyzes optimal row-column designs for mixed-level
factorial experiments under square and rectangular field layouts. For
square field layouts, the package implements direct common-factor
constructions by first forming two component treatment arrays, one for
each factor or super-factor, and then combining them through a symbolic
cell-wise product following Gopinath, Parsad and Mandal (2018)
<doi:10.1080/03610926.2017.1376091>. For rectangular field layouts, the
package constructs designs by extracting a balanced principal block from a
mixed-level block design, treating it as the principal column, taking the
complete treatment set as the principal row, and generating the full
row-column design by cyclic modular development. The package also includes
repair utilities for improving disconnected or partially connected
row-column designs through bounded treatment-swap searches while
preserving the row-column layout structure. The package provides
diagnostic tools for connectedness, orthogonal factorial structure,
balance, estimability, and selected optimality criteria for row-column
designs.

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
