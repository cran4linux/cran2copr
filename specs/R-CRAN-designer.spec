%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  designer
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' UI Prototype Builder

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-golem >= 0.3.1
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-cicerone 
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-shinipsum 
BuildRequires:    R-CRAN-shinyscreenshot 
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-golem >= 0.3.1
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-cicerone 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-shinipsum 
Requires:         R-CRAN-shinyscreenshot 

%description
A 'shiny' application that enables the user to create a prototype UI,
being able to drag and drop UI components before being able to save or
download the equivalent R code.

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
