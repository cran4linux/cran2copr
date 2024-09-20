%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  startR
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Retrieve Multidimensional Distributed Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.1.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-easyNCDF 
BuildRequires:    R-CRAN-s2dv 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-methods 
Requires:         R-CRAN-multiApply >= 2.1.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-future 
Requires:         R-parallel 
Requires:         R-CRAN-easyNCDF 
Requires:         R-CRAN-s2dv 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-CRAN-PCICt 
Requires:         R-methods 

%description
Tool to automatically fetch, transform and arrange subsets of multi-
dimensional data sets (collections of files) stored in local and/or remote
file systems or servers, using multicore capabilities where possible. The
tool provides an interface to perceive a collection of data sets as a
single large multidimensional data array, and enables the user to request
for automatic retrieval, processing and arrangement of subsets of the
large array. Wrapper functions to add support for custom file formats can
be plugged in/out, making the tool suitable for any research field where
large multidimensional data sets are involved.

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
