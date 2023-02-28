%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wildrwolf
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Computation of Romano-Wolf Corrected p-Values for Linear Regression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-fwildclusterboot 
BuildRequires:    R-CRAN-dreamerr 
BuildRequires:    R-CRAN-fabricatr 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-fwildclusterboot 
Requires:         R-CRAN-dreamerr 
Requires:         R-CRAN-fabricatr 
Requires:         R-CRAN-MASS 

%description
Fast Routines to Compute Romano-Wolf corrected p-Values (Romano and Wolf
(2005a) <DOI:10.1198/016214504000000539>, Romano and Wolf (2005b)
<DOI:10.1111/j.1468-0262.2005.00615.x>) for objects of type 'fixest' and
'fixest_multi' from the 'fixest' package via a wild (cluster) bootstrap.

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
