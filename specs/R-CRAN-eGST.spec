%global packname  eGST
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Leveraging eQTLs to Identify Individual-Level Tissue of Interestfor a Complex Trait

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 

%description
Genetic predisposition for complex traits is often manifested through
multiple tissues of interest at different time points in the development.
As an example, the genetic predisposition for obesity could be manifested
through inherited variants that control metabolism through regulation of
genes expressed in the brain and/or through the control of fat storage in
the adipose tissue by dysregulation of genes expressed in adipose tissue.
We present a method eGST (eQTL-based genetic subtyper) that integrates
tissue-specific eQTLs with GWAS data for a complex trait to
probabilistically assign a tissue of interest to the phenotype of each
individual in the study. eGST estimates the posterior probability that an
individual's phenotype can be assigned to a tissue based on
individual-level genotype data of tissue-specific eQTLs and marginal
phenotype data in a genome-wide association study (GWAS) cohort. Under a
Bayesian framework of mixture model, eGST employs a maximum a posteriori
(MAP) expectation-maximization (EM) algorithm to estimate the
tissue-specific posterior probability across individuals. Methodology is
available from: A Majumdar, C Giambartolomei, N Cai, MK Freund, T Haldar,
T Schwarz, J Flint, B Pasaniuc (2019) <doi:10.1101/674226>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
