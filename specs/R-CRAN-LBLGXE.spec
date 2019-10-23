%global packname  LBLGXE
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Logistic Bayesian Lasso for Rare (or Common) HaplotypeAssociation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-hapassoc 
BuildRequires:    R-CRAN-dummies 
Requires:         R-CRAN-hapassoc 
Requires:         R-CRAN-dummies 

%description
This function takes a dataset of haplotypes and environmental covariates
with one binary phenotype in which rows for individuals of uncertain phase
have been augmented by "pseudo-individuals" who carry the possible
multilocus genotypes consistent with the single-locus phenotypes. Bayesian
lasso is used to find the posterior distributions of logistic regression
coefficients, which are then used to calculate Bayes Factor and credible
set to test for association with haplotypes, environmental covariates and
interactions. The model can handle complex sampling data, in particular,
frequency matched cases and controls with controls obtained using
stratified sampling. This version can also be applied to a dataset with no
environmental covariate and two correlated binary phenotypes.

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
%{rlibdir}/%{packname}/libs
