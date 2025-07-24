%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbX
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Microbiome Data Processing Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-tools 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-multcompView 

%description
Provides tools for cleaning, processing, and preparing microbiome
sequencing data (e.g., 16S rRNA) for downstream analysis. Supports CSV,
TXT, and Excel file formats. The main function, ezclean(), automates
microbiome data transformation, including format validation,
transposition, numeric conversion, and metadata integration. It also
handles taxonomic levels efficiently, resolves duplicated taxa entries,
and outputs a well-structured, analysis-ready dataset. The companion
functions ezstat() run statistical tests and summarize results, while
ezviz() produces publication-ready visualizations.

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
