%global packname  CPBayes
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Bayesian Meta Analysis for Studying Cross-Phenotype GeneticAssociations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-forestplot 
Requires:         R-grDevices 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-mvtnorm 

%description
A Bayesian meta-analysis method for studying cross-phenotype genetic
associations. It uses summary-level data across multiple phenotypes to
simultaneously measure the evidence of aggregate-level pleiotropic
association and estimate an optimal subset of traits associated with the
risk locus. CPBayes is based on a spike and slab prior.

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
