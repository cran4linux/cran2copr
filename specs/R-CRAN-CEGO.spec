%global __brp_check_rpaths %{nil}
%global packname  CEGO
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Combinatorial Efficient Global Optimization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-fastmatch 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-DEoptim 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-fastmatch 

%description
Model building, surrogate model based optimization and Efficient Global
Optimization in combinatorial or mixed search spaces.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
