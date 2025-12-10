%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crownsegmentr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tree Crown Segmentation in Airborne LiDAR Point Clouds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-lidR >= 4.0.0
BuildRequires:    R-CRAN-BH >= 1.75.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-lidR >= 4.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
Provides a function that performs the adaptive mean shift algorithm for
individual tree crown delineation in 3D point clouds as proposed by Ferraz
et al. (2016) <doi:10.1016/j.rse.2016.05.028>, as well as supporting
functions.

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
