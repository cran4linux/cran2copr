%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ukbnmr
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Removal of Unwanted Technical Variation from UK Biobank NMR Metabolomics Biomarker Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MASS 

%description
A suite of utilities for working with the UK Biobank
<https://www.ukbiobank.ac.uk/> Nuclear Magnetic Resonance spectroscopy
(NMR) metabolomics data
<https://biobank.ndph.ox.ac.uk/showcase/label.cgi?id=220>. Includes
functions for extracting biomarkers from decoded UK Biobank field data,
removing unwanted technical variation from biomarker concentrations,
computing an extended set of lipid, fatty acid, and cholesterol fractions,
and for re-deriving composite biomarkers and ratios after adjusting data
for unwanted biological variation. For further details on methods see
Ritchie SC et al. Sci Data (2023) <doi:10.1038/s41597-023-01949-y>.

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
