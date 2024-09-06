%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datamods
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Modules to Import and Manipulate Data in 'Shiny'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.8.4
BuildRequires:    R-CRAN-toastui >= 0.3.3
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-phosphoricons 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-shinyWidgets >= 0.8.4
Requires:         R-CRAN-toastui >= 0.3.3
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-phosphoricons 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-writexl 

%description
'Shiny' modules to import data into an application or 'addin' from various
sources, and to manipulate them after that.

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
