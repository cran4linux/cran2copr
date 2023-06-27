%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedsuite
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Installation of the 'ped suite' Packages for Pedigree Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forrel 
BuildRequires:    R-CRAN-pedprobr 
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-ribd 
BuildRequires:    R-CRAN-verbalisr 
BuildRequires:    R-CRAN-pedmut 
BuildRequires:    R-CRAN-dvir 
BuildRequires:    R-CRAN-ibdsim2 
BuildRequires:    R-CRAN-paramlink2 
BuildRequires:    R-CRAN-pedbuildr 
BuildRequires:    R-CRAN-segregatr 
Requires:         R-CRAN-forrel 
Requires:         R-CRAN-pedprobr 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-ribd 
Requires:         R-CRAN-verbalisr 
Requires:         R-CRAN-pedmut 
Requires:         R-CRAN-dvir 
Requires:         R-CRAN-ibdsim2 
Requires:         R-CRAN-paramlink2 
Requires:         R-CRAN-pedbuildr 
Requires:         R-CRAN-segregatr 

%description
The 'ped suite' is a collection of packages for pedigree analysis,
covering applications in forensic genetics, medical genetics and more. A
detailed presentation of the 'ped suite' is given in the book 'Pedigree
Analysis in R' (Vigeland, 2021, ISBN: 9780128244302).

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
