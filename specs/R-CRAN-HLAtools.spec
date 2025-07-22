%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HLAtools
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for HLA Immunogenomics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-rvest 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-xfun 

%description
A toolkit for the analysis and management of data for genes in the
so-called "Human Leukocyte Antigen" (HLA) region. Functions extract
reference data from the Anthony Nolan HLA Informatics Group/ImmunoGeneTics
HLA 'GitHub' repository (ANHIG/IMGTHLA)
<https://github.com/ANHIG/IMGTHLA>, validate Genotype List (GL) Strings,
convert between UNIFORMAT and GL String Code (GLSC) formats, translate HLA
alleles and GLSCs across ImmunoPolymorphism Database (IPD) IMGT/HLA
Database release versions, identify differences between pairs of alleles
at a locus, generate customized, multi-position sequence alignments, trim
and convert allele-names across nomenclature epochs, and extend existing
data-analysis methods.

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
