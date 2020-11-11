%global packname  discord
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Discordant Kinship Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-janitor 
Requires:         R-stats 
Requires:         R-CRAN-broom 

%description
Functions for discordant kinship modeling (and other sibling-based
quasi-experimental designs). Currently, the package contains data
restructuring functions and functions for generating biometrically
informed data for kin pairs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
