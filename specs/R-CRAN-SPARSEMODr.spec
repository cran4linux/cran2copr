%global packname  SPARSEMODr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SPAtial Resolution-SEnsitive Models of Outbreak Dynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-geosphere 

%description
Implementation of spatially-explicit, stochastic disease models with
customizable time windows that describe how parameter values fluctuate
during outbreaks (e.g., in response to public health or conservation
interventions).

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
