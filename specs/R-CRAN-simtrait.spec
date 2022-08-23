%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simtrait
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Complex Traits from Genotypes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PRROC 
Requires:         R-CRAN-PRROC 

%description
Simulate complex traits given a SNP genotype matrix and model parameters
(the desired heritability, number of causal loci, and either the true
ancestral allele frequencies used to generate the genotypes or the mean
kinship for a real dataset).  Emphasis on avoiding common biases due to
the use of estimated allele frequencies.  The code selects random loci to
be causal, constructs coefficients for these loci and random independent
non-genetic effects, and can optionally generate random group effects.
Traits can follow three models: random coefficients, fixed effect sizes,
and infinitesimal (multivariate normal).  GWAS method benchmarking
functions are also provided.  Described in Yao and Ochoa (2022)
<doi:10.1101/2022.03.25.485885>.

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
