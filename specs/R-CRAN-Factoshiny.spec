%global __brp_check_rpaths %{nil}
%global packname  Factoshiny
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Factorial Analysis from 'FactoMineR' with a Shiny Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR >= 2.3
BuildRequires:    R-CRAN-FactoInvestigate >= 1.5
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-grDevices 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-missMDA 
Requires:         R-CRAN-FactoMineR >= 2.3
Requires:         R-CRAN-FactoInvestigate >= 1.5
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-colourpicker 
Requires:         R-grDevices 
Requires:         R-tcltk 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-missMDA 

%description
Perform factorial analysis with a menu and draw graphs interactively
thanks to 'FactoMineR' and a Shiny application.

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
