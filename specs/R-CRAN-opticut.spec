%global packname  opticut
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Likelihood Based Optimal Partitioning and Indicator SpeciesAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-CRAN-ResourceSelection >= 0.3.2
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mefa4 
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-CRAN-ResourceSelection >= 0.3.2
Requires:         R-MASS 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-betareg 
Requires:         R-parallel 
Requires:         R-CRAN-mefa4 

%description
Likelihood based optimal partitioning and indicator species analysis.
Finding the best binary partition for each species based on model
selection, with the possibility to take into account modifying/confounding
variables as described in Kemencei et al. (2014)
<doi:10.1556/ComEc.15.2014.2.6>. The package implements binary and
multi-level response models, various measures of uncertainty, Lorenz-curve
based thresholding, with native support for parallel computations.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
