%global __brp_check_rpaths %{nil}
%global packname  RVFam
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Rare Variants Association Analyses with Family Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-coxme 
Requires:         R-survival 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-kinship2 
Requires:         R-MASS 
Requires:         R-Matrix 

%description
The RVFam package provides functions to perform single SNP association
analyses and gene-based tests for continuous, binary and survival traits
against sequencing data (e.g. exome chip) using family data.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
