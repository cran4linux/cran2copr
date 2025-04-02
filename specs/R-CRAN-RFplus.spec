%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RFplus
%global packver   1.5-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning for Merging Satellite and Ground Precipitation Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-qmap 
BuildRequires:    R-CRAN-hydroGOF 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-qmap 
Requires:         R-CRAN-hydroGOF 

%description
A machine learning algorithm that merges satellite and ground
precipitation data using Random Forest for spatial prediction, residual
modeling for bias correction, and quantile mapping for adjustment,
ensuring accurate estimates across temporal scales and regions.

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
