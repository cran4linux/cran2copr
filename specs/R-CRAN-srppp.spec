%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  srppp
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Read the Swiss Register of Plant Protection Products

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dm 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dm 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-rlang 

%description
Generate data objects from XML versions of the Swiss Register of Plant
Protection Products. An online version of the register can be accessed at
<https://www.psm.admin.ch/de/produkte>. There is no guarantee of
correspondence of the data read in using this package with that online
version, or with the original registration documents.  Also, the Federal
Food Safety and Veterinary Office, coordinating the authorisation of plant
protection products in Switzerland, does not answer requests regarding
this package.

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
