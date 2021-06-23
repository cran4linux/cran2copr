%global __brp_check_rpaths %{nil}
%global packname  StrathE2E2
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          End-to-End Marine Food Web Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NetIndices 
Requires:         R-CRAN-deSolve 
Requires:         R-methods 
Requires:         R-CRAN-NetIndices 

%description
A dynamic model of the big-picture, whole ecosystem effects of
hydrodynamics, temperature, nutrients, and fishing on continental shelf
marine food webs. The package is described in: Heath, M.R., Speirs, D.C.,
Thurlbeck, I. and Wilson, R.J. (2020) <doi:10.1111/2041-210X.13510>
StrathE2E2: An R package for modelling the dynamics of marine food webs
and fisheries. 8pp.

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
