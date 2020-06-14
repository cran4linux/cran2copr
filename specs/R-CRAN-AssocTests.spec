%global packname  AssocTests
%global packver   0.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          2%{?dist}
Summary:          Genetic Association Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-fExtremes 
Requires:         R-cluster 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-fExtremes 

%description
Some procedures including EIGENSTRAT (a procedure for detecting and
correcting for population stratification through searching for the
eigenvectors in genetic association studies), PCoC (a procedure for
correcting for population stratification through calculating the principal
coordinates and the clustering of the subjects), Tracy-Widom test (a
procedure for detecting the significant eigenvalues of a matrix), distance
regression (a procedure for detecting the association between a distance
matrix and some independent variants of interest), single-marker test (a
procedure for identifying the association between the genotype at a
biallelic marker and a trait using the Wald test or the Fisher's exact
test), MAX3 (a procedure for testing for the association between a single
nucleotide polymorphism and a binary phenotype using the maximum value of
the three test statistics derived for the recessive, additive, and
dominant models), nonparametric trend test (a procedure for testing for
the association between a genetic variant and a non-normal distributed
quantitative trait based on the nonparametric risk), and nonparametric
MAX3 (a procedure for testing for the association between a biallelic
single nucleotide polymorphism and a quantitative trait using the maximum
value of the three nonparametric trend tests derived for the recessive,
additive, and dominant models), which are commonly used in genetic
association studies.

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
