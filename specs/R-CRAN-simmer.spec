%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simmer
%global packver   4.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete-Event Simulation for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-codetools 
Requires:         R-utils 

%description
A process-oriented and trajectory-based Discrete-Event Simulation (DES)
package for R. It is designed as a generic yet powerful framework. The
architecture encloses a robust and fast simulation core written in 'C++'
with automatic monitoring capabilities. It provides a rich and flexible R
API that revolves around the concept of trajectory, a common path in the
simulation model for entities of the same type. Documentation about
'simmer' is provided by several vignettes included in this package, via
the paper by Ucar, Smeets & Azcorra (2019, <doi:10.18637/jss.v090.i02>),
and the paper by Ucar, Hernández, Serrano & Azcorra (2018,
<doi:10.1109/MCOM.2018.1700960>); see 'citation("simmer")' for details.

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
