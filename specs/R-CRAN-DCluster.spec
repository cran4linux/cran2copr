%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DCluster
%global packver   0.2-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for the Detection of Spatial Clusters of Diseases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.6.2
Requires:         R-core >= 1.6.2
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 

%description
A set of functions for the detection of spatial clusters of disease using
count data. Bootstrap is used to estimate sampling distributions of
statistics.

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
