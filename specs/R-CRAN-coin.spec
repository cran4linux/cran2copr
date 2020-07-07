%global packname  coin
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}
Summary:          Conditional Inference Procedures in a Permutation Test Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-libcoin >= 1.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-CRAN-modeltools >= 0.2.9
BuildRequires:    R-survival 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-libcoin >= 1.0.0
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-CRAN-modeltools >= 0.2.9
Requires:         R-survival 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-CRAN-multcomp 

%description
Conditional inference procedures for the general independence problem
including two-sample, K-sample (non-parametric ANOVA), correlation,
censored, ordered and multivariate problems.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/doxygen.cfg
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
