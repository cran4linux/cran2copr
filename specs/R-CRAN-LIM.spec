%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LIM
%global packver   1.4.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Inverse Model Examples and Solution Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildArch:        noarch
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-graphics 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-diagram 
Requires:         R-graphics 

%description
Functions that read and solve linear inverse problems (food web problems,
linear programming problems). These problems find solutions to linear or
quadratic functions: min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) =
sum(ai*xi) subject to equality constraints Ex=f and inequality constraints
Gx>=h.

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
