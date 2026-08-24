%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightedScores
%global packver   0.9.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Scores Method for Regression Models with Dependent Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rootSolve 

%description
The weighted scores method and composite likelihood information criteria
as an intermediate step for variable/correlation selection for
longitudinal ordinal and count data in Nikoloulopoulos, Joe and Chaganty
(2011) <doi:10.1093/biostatistics/kxr005>, Nikoloulopoulos (2016)
<doi:10.1002/sim.6871> and Nikoloulopoulos (2017)
<doi:10.1080/00949655.2020.1759602>.

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
