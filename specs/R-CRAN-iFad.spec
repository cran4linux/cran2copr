%global __brp_check_rpaths %{nil}
%global packname  iFad
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          An integrative factor analysis model for drug-pathwayassociation inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ROCR 
Requires:         R-CRAN-Rlab 
Requires:         R-MASS 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ROCR 

%description
This package implements a Bayesian sparse factor model for the joint
analysis of paired datasets, one is the gene expression dataset and the
other is the drug sensitivity profiles, measured across the same panel of
samples, e.g., cell lines. Prior knowledge about gene-pathway associations
can be easily incorporated in the model to aid the inference of
drug-pathway associations.

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
