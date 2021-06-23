%global __brp_check_rpaths %{nil}
%global packname  haplotyper
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tool for Clustering Genotypes in Haplotypes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-utils 

%description
Function to identify haplotypes within QTL (Quantitative Trait Loci). One
haplotype is a combination of SNP (Single Nucleotide Polymorphisms) within
the QTL. This function groups together all individuals of a population
with the same haplotype. Each group contains individual with the same
allele in each SNP, whether or not missing data. Thus, haplotyper groups
individuals, that to be imputed, have a non-zero probability of having the
same alleles in the entire sequence of SNP's. Moreover, haplotyper
calculates such probability from relative frequencies.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
