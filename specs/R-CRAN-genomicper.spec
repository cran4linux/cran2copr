%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genomicper
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Circular Genomic Permutation using Genome Wide Association p-Values

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 

%description
Circular genomic permutation approach uses genome wide association studies
(GWAS) results to establish the significance of pathway/gene-set
associations whilst accounting for genomic structure. All single
nucleotide polymorphisms (SNPs) in the GWAS are placed in a 'circular
genome' according to their location. Then the complete set of SNP
association p-values are permuted by rotation with respect to the SNPs'
genomic locations. Two testing frameworks are available: permutations at
the gene level, and permutations at the SNP level. The permutation at the
gene level uses Fisher's combination test to calculate a single gene
p-value, followed by the hypergeometric test. The SNP count methodology
maps each SNP to pathways/gene-sets and calculates the proportion of SNPs
for the real and the permutated datasets above a pre-defined threshold.
Genomicper requires a matrix of GWAS association p-values and SNPs
annotation to genes. Pathways can be obtained from within the package or
can be provided by the user. Cabrera et al (2012)
<doi:10.1534/g3.112.002618> .

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
