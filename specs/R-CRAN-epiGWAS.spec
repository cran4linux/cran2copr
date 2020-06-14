%global packname  epiGWAS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Robust Methods for Epistasis Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-SNPknock 
BuildRequires:    R-parallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-SNPknock 
Requires:         R-parallel 

%description
Functions to perform robust epistasis detection in genome-wide association
studies, as described in Slim et al. (2018) <doi:10.1101/442749>. The
implemented methods identify pairwise interactions between a particular
target variant and the rest of the genotype, using a propensity score
approach. The propensity score models the linkage disequilibrium between
the target and the rest of the genotype. All methods are penalized
regression approaches, which differently incorporate the propensity score
to only recover the synergistic effects between the target and the
genotype.

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
%{rlibdir}/%{packname}/INDEX
