%global packname  BRISC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Inference for Large Spatial Datasets using BRISC

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rdist 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-graphics 
Requires:         R-CRAN-RANN 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-rdist 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-pbapply 
Requires:         R-graphics 

%description
Fits bootstrap with univariate spatial regression models using Bootstrap
for Rapid Inference on Spatial Covariances (BRISC) for large datasets
using nearest neighbor Gaussian processes detailed in Saha and Datta
(2018) <doi:10.1002/sta4.184>.

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
