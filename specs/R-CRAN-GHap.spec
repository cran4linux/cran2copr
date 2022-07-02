%global __brp_check_rpaths %{nil}
%global packname  GHap
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Haplotyping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-class >= 7.3.15
BuildRequires:    R-parallel >= 3.4.4
BuildRequires:    R-methods >= 3.4.4
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-Matrix >= 1.2.16
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-pedigreemm >= 0.3.3
BuildRequires:    R-CRAN-sparseinv >= 0.1.3
Requires:         R-CRAN-class >= 7.3.15
Requires:         R-parallel >= 3.4.4
Requires:         R-methods >= 3.4.4
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-Matrix >= 1.2.16
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-pedigreemm >= 0.3.3
Requires:         R-CRAN-sparseinv >= 0.1.3

%description
Haplotype calling from phased marker data. Given user-defined haplotype
blocks (HapBlock), the package identifies the different haplotype alleles
(HapAllele) present in the data and scores sample haplotype allele
genotypes (HapGenotype) based on HapAllele dose (i.e. 0, 1 or 2 copies).
The output is not only useful for analyses that can handle multi-allelic
markers, but is also conveniently formatted for existing pipelines
intended for bi-allelic markers. The package was first described in
Bioinformatics by Utsunomiya et al. (2016,
<doi:10.1093/bioinformatics/btw356>). Since the v2 release, the package
provides functions for unsupervised and supervised detection of ancestry
tracks. The methods implemented in these functions were described in an
article published in Methods in Ecology and Evolution by Utsunomiya et al.
(2020, <doi:10.1111/2041-210X.13467>). The source code for v3 was modified
for improved performance and inclusion of new functionality, including
analysis of unphased data, runs of homozygosity, sampling methods for
virtual gamete mating, mixed model fitting and GWAS.

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
