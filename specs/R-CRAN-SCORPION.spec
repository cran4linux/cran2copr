%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCORPION
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Single Cell Oriented Reconstruction of PANDA Individual Optimized Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RhpcBLASctl 

%description
Constructs gene regulatory networks from single-cell gene expression data
using the PANDA (Passing Attributes between Networks for Data
Assimilation) algorithm.

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
