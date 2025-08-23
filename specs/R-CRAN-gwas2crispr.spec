%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gwas2crispr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          GWAS-to-CRISPR Data Pipeline for High-Throughput SNP Target Extraction

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-methods 

%description
Provides a reproducible pipeline to conduct genome‑wide association
studies (GWAS) and extract single‑nucleotide polymorphisms (SNPs) for a
human trait or disease. Given aggregated GWAS dataset(s) and a
user‑defined significance threshold, the package retrieves significant
SNPs from the GWAS Catalog and the Experimental Factor Ontology (EFO),
annotates their gene context, and can write a harmonised metadata table in
comma-separated values (CSV) format, genomic intervals in the Browser
Extensible Data (BED) format, and sequences in the FASTA (text-based
sequence) format with user-defined flanking regions for clustered
regularly interspaced short palindromic repeats (CRISPR) guide design. For
details on the resources and methods see: Buniello et al. (2019)
<doi:10.1093/nar/gky1120>; Sollis et al. (2023)
<doi:10.1093/nar/gkac1010>; Jinek et al. (2012)
<doi:10.1126/science.1225829>; Malone et al. (2010)
<doi:10.1093/bioinformatics/btq099>; Experimental Factor Ontology (EFO)
<https://www.ebi.ac.uk/efo>.

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
