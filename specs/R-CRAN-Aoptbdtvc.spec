%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Aoptbdtvc
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          A-Optimal Block Designs for Comparing Test Treatments with Controls

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-MASS 

%description
A collection of functions to construct A-optimal block designs for
comparing test treatments with one or more control(s). Mainly A-optimal
balanced treatment incomplete block designs, weighted A-optimal balanced
treatment incomplete block designs, A-optimal group divisible treatment
designs and A-optimal balanced bipartite block designs can be constructed
using the package. The designs are constructed using algorithms based on
linear integer programming. To the best of our knowledge, these facilities
to construct A-optimal block designs for comparing test treatments with
one or more controls are not available in the existing R packages. For
more details on designs for tests versus control(s) comparisons, please
see Hedayat, A. S. and Majumdar, D. (1984)
<doi:10.1080/00401706.1984.10487989> A-Optimal Incomplete Block Designs
for Control-Test Treatment Comparisons, Technometrics, 26, 363-370 and
Mandal, B. N. , Gupta, V. K., Parsad, Rajender. (2017)
<doi:10.1080/03610926.2015.1071394> Balanced treatment incomplete block
designs through integer programming. Communications in Statistics - Theory
and Methods 46(8), 3728-3737.

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
