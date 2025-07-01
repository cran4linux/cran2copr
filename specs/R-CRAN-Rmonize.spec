%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmonize
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Data Harmonization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-fabR >= 2.0.0
BuildRequires:    R-CRAN-madshapR >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-fabR >= 2.0.0
Requires:         R-CRAN-madshapR >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-haven 
Requires:         R-utils 
Requires:         R-CRAN-fs 

%description
Integrated tools to support rigorous and well documented data
harmonization based on Maelstrom Research guidelines. The package includes
functions to assess and prepare input elements, apply specified processing
rules to generate harmonized datasets, validate data processing and
identify processing errors, and document and summarize harmonized outputs.
The harmonization process is defined and structured by two key
user-generated documents: the DataSchema (specifying the list of
harmonized variables to generate across datasets) and the Data Processing
Elements (specifying the input elements and processing algorithms to
generate harmonized variables in DataSchema formats). The package was
developed to address key challenges of retrospective data harmonization in
epidemiology (as described in Fortier I and al. (2017)
<doi:10.1093/ije/dyw075>) but can be used for any data harmonization
initiative.

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
