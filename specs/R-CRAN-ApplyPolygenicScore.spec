%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ApplyPolygenicScore
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for the Application of a Polygenic Score to a VCF

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-BoutrosLab.plotting.general 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-BoutrosLab.plotting.general 
Requires:         R-CRAN-lattice 

%description
Simple and transparent parsing of genotype/dosage data from an input
Variant Call Format (VCF) file, matching of genotype coordinates to the
component Single Nucleotide Polymorphisms (SNPs) of an existing polygenic
score (PGS), and application of SNP weights to dosages for the calculation
of a polygenic score for each individual in accordance with the additive
weighted sum of dosages model. Methods are designed in reference to best
practices described by Collister, Liu, and Clifton (2022)
<doi:10.3389/fgene.2022.818574>.

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
