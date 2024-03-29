%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynatopGIS
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithms for Helping Build Dynamic TOPMODEL Implementations from Spatial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-terra 
Requires:         R-methods 
Requires:         R-CRAN-jsonlite 

%description
A set of algorithms based on Quinn et al. (1991)
<doi:10.1002/hyp.3360050106> for processing river network and digital
elevation data to build implementations of Dynamic TOPMODEL, a
semi-distributed hydrological model proposed in Beven and Freer (2001)
<doi:10.1002/hyp.252>. The 'dynatop' package implements simulation code
for Dynamic TOPMODEL based on the output of 'dynatopGIS'.

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
