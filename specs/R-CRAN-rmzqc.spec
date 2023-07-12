%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmzqc
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Creation, Reading and Validation of 'mzqc' Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ontologyIndex 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-R6P 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-tools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-ontologyIndex 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-R6P 
Requires:         R-CRAN-testthat 
Requires:         R-tools 

%description
Reads, writes and validates 'mzQC' files. The 'mzQC' format is a
standardized file format for the exchange, transmission, and archiving of
quality metrics derived from biological mass spectrometry data, as defined
by the HUPO-PSI (Human Proteome Organisation - Proteomics Standards
Initiative) Quality Control working group. See
<https://hupo-psi.github.io/mzQC/> for details.

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
