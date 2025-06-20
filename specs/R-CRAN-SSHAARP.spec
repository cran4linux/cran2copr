%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSHAARP
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Searching Shared HLA Amino Acid Residue Prevalence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       ghostscript
Recommends:       gmt
BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-gmt 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-filesstrings 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-HLAtools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-gmt 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-filesstrings 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-HLAtools 

%description
Processes amino acid alignments produced by the 'IPD-IMGT/HLA (Immuno
Polymorphism-ImMunoGeneTics/Human Leukocyte Antigen) Database' to identify
user-defined amino acid residue motifs shared across HLA alleles, HLA
alleles, or HLA haplotypes, and calculates frequencies based on HLA allele
frequency data. 'SSHAARP' (Searching Shared HLA Amino Acid Residue
Prevalence) uses 'Generic Mapping Tools (GMT)' software and the 'GMT' R
package to generate global frequency heat maps that illustrate the
distribution of each user-defined map around the globe. 'SSHAARP' analyzes
the allele frequency data described by Solberg et al. (2008)
<doi:10.1016/j.humimm.2008.05.001>, a global set of 497 population samples
from 185 published datasets, representing 66,800 individuals total. Users
may also specify their own datasets, but file conventions must follow the
prebundled Solberg dataset, or the mock haplotype dataset.

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
