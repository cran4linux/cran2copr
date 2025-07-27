%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nprcgenekeepr
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Tools for Colony Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-Rlabkey 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-WriteXLS 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-Rlabkey 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-WriteXLS 

%description
Provides genetic tools for colony management and is a derivation of the
work in Amanda Vinson and Michael J Raboin (2015)
<https://pmc.ncbi.nlm.nih.gov/articles/PMC4671785/> "A Practical Approach
for Designing Breeding Groups to Maximize Genetic Diversity in a Large
Colony of Captive Rhesus Macaques ('Macaca' 'mulatto')". It provides a
'Shiny' application with an exposed API. The application supports five
groups of functions: (1) Quality control of studbooks contained in text
files or 'Excel' workbooks and of pedigrees within 'LabKey' Electronic
Health Records (EHR); (2) Creation of pedigrees from a list of animals
using the 'LabKey' EHR integration; (3) Creation and display of an age by
sex pyramid plot of the living animals within the designated pedigree; (4)
Generation of genetic value analysis reports; and (5) Creation of
potential breeding groups with and without proscribed sex ratios and
defined maximum kinships.

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
