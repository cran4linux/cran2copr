%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  invacost
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Biological Invasion Costs with the 'InvaCost' Database

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-grDevices 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an up-to-date version of the 'InvaCost' database
(<doi:10.6084/m9.figshare.12668570>) in R, and several functions to
analyse the costs of invasive alien species
(<doi:10.1111/2041-210X.13929>).

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
