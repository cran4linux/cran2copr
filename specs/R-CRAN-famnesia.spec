%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  famnesia
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Anonymising Familias Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.9.0
BuildRequires:    R-CRAN-pedprobr >= 1.1.1
BuildRequires:    R-CRAN-pedFamilias >= 0.2.6
BuildRequires:    R-CRAN-bslib >= 0.11.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-pedmut 
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-shiny >= 1.9.0
Requires:         R-CRAN-pedprobr >= 1.1.1
Requires:         R-CRAN-pedFamilias >= 0.2.6
Requires:         R-CRAN-bslib >= 0.11.0
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-pedmut 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-shinyjs 

%description
A 'shiny' application for anonymising files exported from the 'Familias'
software for forensic kinship analysis (Egeland et al. (2000)
<doi:10.1016/s0379-0738(00)00147-x>). Pedigrees, marker data, allele
frequencies and mutation models can be masked or modified, with options
for preserving likelihood ratios exactly. The application is built on the
'pedsuite' packages for pedigree analysis.

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
