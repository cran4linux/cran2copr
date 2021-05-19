%global packname  spatialrisk
%global packver   0.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Spatial Risk

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-geohashTools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tmap 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-vroom 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-geohashTools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mapview 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tmap 
Requires:         R-CRAN-units 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-vroom 

%description
Methods for spatial risk calculations. It offers an efficient approach to
determine the sum of all observations within a circle of a certain radius.
This might be beneficial for insurers who are required (by a recent
European Commission regulation) to determine the maximum value of insured
fire risk policies of all buildings that are partly or fully located
within a circle of a radius of 200m. See Church (1974)
<doi:10.1007/BF01942293> for a description of the problem.

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
