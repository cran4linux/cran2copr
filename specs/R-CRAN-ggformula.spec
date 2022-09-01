%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggformula
%global packver   0.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.2
Release:          1%{?dist}%{?buildtag}
Summary:          Formula Interface to the Grammar of Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-mosaicCore >= 0.7.0
BuildRequires:    R-CRAN-ggstance >= 0.3.4
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-labelled 
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-mosaicCore >= 0.7.0
Requires:         R-CRAN-ggstance >= 0.3.4
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggforce 
Requires:         R-grid 
Requires:         R-CRAN-labelled 

%description
Provides a formula interface to 'ggplot2' graphics.

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
