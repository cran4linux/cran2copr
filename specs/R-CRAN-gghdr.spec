%global __brp_check_rpaths %{nil}
%global packname  gghdr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation of Highest Density Regions in 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-hdrcde 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-digest 

%description
Provides 'ggplot2' framework for visualising Highest Density Regions (HDR)
<doi:10.1080/00031305.1996.10474359>. This work is based on the package
'hdrcde'<https://pkg.robjhyndman.com/hdrcde/> and displays highest density
regions in 'ggplot2' for one and two dimensions and univariate densities
conditional on one covariate.

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
