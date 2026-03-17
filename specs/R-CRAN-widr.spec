%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  widr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the World Inequality Database (WID)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-scales 
Requires:         R-tools 
Requires:         R-utils 

%description
Interface to the World Inequality Database (WID) API <https://wid.world>.
Downloads distributional national accounts data with filters for country,
year, percentile, age group, and population type. Includes code validation
and reference tables. Independent implementation unaffiliated with the
World Inequality Lab (WIL) or the Paris School of Economics.

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
