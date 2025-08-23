%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cffdrs
%global packver   1.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Canadian Forest Fire Danger Rating System

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-geosphere 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
This project provides a group of new functions to calculate the outputs of
the two main components of the Canadian Forest Fire Danger Rating System
(CFFDRS) Van Wagner and Pickett (1985)
<https://ostrnrcan-dostrncan.canada.ca/entities/publication/29706108-2891-4e5d-a59a-a77c96bc507c>)
at various time scales: the Fire Weather Index (FWI) System Wan Wagner
(1985)
<https://ostrnrcan-dostrncan.canada.ca/entities/publication/d96e56aa-e836-4394-ba29-3afe91c3aa6c>
and the Fire Behaviour Prediction (FBP) System Forestry Canada Fire Danger
Group (1992) <https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/10068.pdf>. Some
functions have two versions, table and raster based.

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
