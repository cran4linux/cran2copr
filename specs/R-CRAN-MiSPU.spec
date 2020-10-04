%global packname  MiSPU
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Microbiome Based Sum of Powered Score (MiSPU) Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-aSPU 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-aSPU 
Requires:         R-cluster 

%description
There is an increasing interest in investigating how the compositions of
microbial communities are associated with human health and disease. In
this package, we present a novel global testing method called aMiSPU, that
is highly adaptive and thus high powered across various scenarios,
alleviating the issue with the choice of a phylogenetic distance. Our
simulations and real data analysis demonstrated that aMiSPU test was often
more powerful than several competing methods while correctly controlling
type I error rates.

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
