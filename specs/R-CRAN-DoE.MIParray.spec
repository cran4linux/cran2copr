%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DoE.MIParray
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Creation of Arrays by Mixed Integer Programming

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-DoE.base 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-DoE.base 

%description
'CRAN' packages 'DoE.base' and 'Rmosek' and non-'CRAN' package 'gurobi'
are enhanced with functionality for the creation of optimized arrays for
experimentation, where optimization is in terms of generalized minimum
aberration. It is also possible to optimally extend existing arrays to
larger run size. The package writes 'MPS' (Mathematical Programming
System) files for use with any mixed integer optimization software that
can process such files. If at least one of the commercial products
'Gurobi' or 'Mosek' (free academic licenses available for both) is
available, the package also creates arrays by optimization. For installing
'Gurobi' and its R package 'gurobi', follow instructions at
<https://www.gurobi.com/products/gurobi-optimizer/> and
<https://www.gurobi.com/documentation/7.5/refman/r_api_overview.html> (or
higher version). For installing 'Mosek' and its R package 'Rmosek', follow
instructions at <https://www.mosek.com/downloads/> and
<https://docs.mosek.com/8.1/rmosek/install-interface.html>, or use the
functionality in the stump CRAN R package 'Rmosek'.

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
