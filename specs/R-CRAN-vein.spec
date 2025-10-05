%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vein
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vehicular Emissions Inventories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sf >= 1.0.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dotCall64 
BuildRequires:    R-CRAN-cptcity 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sf >= 1.0.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-units 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-dotCall64 
Requires:         R-CRAN-cptcity 
Requires:         R-grDevices 

%description
Elaboration of vehicular emissions inventories, consisting in four stages,
pre-processing activity data, preparing emissions factors, estimating the
emissions and post-processing of emissions in maps and databases. More
details in Ibarra-Espinosa et al (2018) <doi:10.5194/gmd-11-2209-2018>.
Before using VEIN you need to know the vehicular composition of your study
area, in other words, the combination of of type of vehicles, size and
fuel of the fleet. Then, it is recommended to start with the project to
download a template to create a structure of directories and scripts.

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
