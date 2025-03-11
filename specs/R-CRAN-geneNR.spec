%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geneNR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Gene Identification for Post-GWAS Analysis

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-writexl 

%description
Facilitates the post-Genome Wide Association Studies (GWAS) analysis of
identifying candidate genes within user-defined search window, based on
the identified Single Nucleotide Polymorphisms (SNPs) as given by Mazumder
AK (2024) <doi:10.1038/s41598-024-66903-3>. It supports candidate gene
analysis for wheat and rice. Just import your GWAS result as explained in
the sample_data file and the function does all the manual search and
retrieve candidate genes for you, while exporting the results into
ready-to-use output.

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
