%global packname  genomicper
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          2%{?dist}
Summary:          Circular Genomic Permutation using Gwas p-Values of Association

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-DBI 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-DBI 

%description
Circular genomic permutation approach uses GWAS results to establish the
significance of pathway/gene-set associations whilst accounting for
genomic structure. All SNPs in the GWAS are placed in a 'circular genome'
according to their location. Then the complete set of SNP association
p-values are permuted by rotation with respect to the SNPs' genomic
locations. Two testing frameworks are available: permutations at the gene
level, and permutations at the SNP level. The permutation at the gene
level uses fisher's combination test to calculate a single gene p-value,
followed by the hypergeometric test. The SNP count methodology maps each
SNP to pathways/gene-sets and calculates the proportion of SNPs for the
real and the permutated datasets above a pre-defined threshold. Genomicper
requires a matrix of GWAS association p-values. The SNPs annotation and
pathways annotations can be performed within the package or provided by
the user.

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
%{rlibdir}/%{packname}/INDEX
