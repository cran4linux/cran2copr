%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpaDES.tools
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Additional Tools for Developing Spatially Explicit Discrete Event Simulation (SpaDES) Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-reproducible >= 2.0.9
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-fpCompare >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-reproducible >= 2.0.9
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-fpCompare >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-backports 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Provides GIS and map utilities, plus additional modeling tools for
developing cellular automata, dynamic raster models, and agent based
models in 'SpaDES'. Included are various methods for spatial spreading,
spatial agents, GIS operations, random map generation, and others. See
'?SpaDES.tools' for an categorized overview of these additional tools. The
suggested package 'NLMR' can be installed from the following repository:
(<https://PredictiveEcology.r-universe.dev>).

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
