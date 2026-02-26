%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HaploDiploidEquilibrium
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate F Statistics Using Mixed Haploid and Diploid Organism Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 

%description
Provides functions to estimate population genetics summary statistics from
haplo-diploid systems, where one sex is haploid and the other diploid
(e.g. Hymenoptera insects). It implements a theoretical model assuming
equal sex ratio, random mating, no selection, no mutation, and no gene
flow, deriving expected genotype frequencies for both sexes under these
equilibrium conditions. The package includes windowed calculations
(operating over genomic sliding windows from VCF input) for allele and
genotype frequencies, the inbreeding coefficient (Fis), pairwise Fst,
Nei's H (gene diversity), Watterson's Theta, and sex-specific reference
allele frequencies. Most statistics are agnostic to ploidy, allowing the
package to be applied to both strictly haplo-diploid and fully diploid
systems.

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
