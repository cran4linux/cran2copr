%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabulapdf
%global packver   1.0.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Tables from PDF Documents

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-png 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rJava 
Requires:         R-tools 
Requires:         R-utils 

%description
Bindings for the 'Tabula' <https://tabula.technology/> 'Java' library,
which can extract tables from PDF files. This tool can reduce time and
effort in data extraction processes in fields like investigative
journalism. It allows for automatic and manual table extraction, the
latter facilitated through a 'Shiny' interface, enabling manual areas
selection with a computer mouse for data retrieval.

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
