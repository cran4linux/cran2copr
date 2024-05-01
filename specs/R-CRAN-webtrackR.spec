%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  webtrackR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Preprocessing and Analyzing Web Tracking Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-adaR 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-adaR 
Requires:         R-CRAN-httr 

%description
Data structures and methods to work with web tracking data. The functions
cover data preprocessing steps, enriching web tracking data with external
information and methods for the analysis of digital behavior as used in
several academic papers (e.g., Clemm von Hohenberg et al., 2023
<doi:10.17605/OSF.IO/M3U9P>; Stier et al., 2022
<doi:10.1017/S0003055421001222>).

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
