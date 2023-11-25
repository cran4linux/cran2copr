%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StormR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing the Behaviour of Wind Generated by Tropical Storms and Cyclones

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Set of functions to quantify and map the behaviour of winds generated by
tropical storms and cyclones in space and time. It includes functions to
compute and analyze fields such as the maximum sustained wind field, power
dissipation index and duration of exposure to winds above a given
threshold. It also includes functions to map the trajectories as well as
characteristics of the storms.

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
