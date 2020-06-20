%global packname  mashr
%global packver   0.2.38
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.38
Release:          1%{?dist}
Summary:          Multivariate Adaptive Shrinkage

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-ashr >= 2.2.22
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rmeta 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-ashr >= 2.2.22
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-assertthat 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rmeta 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-abind 

%description
Implements the multivariate adaptive shrinkage (mash) method of Urbut et
al (2019) <DOI:10.1038/s41588-018-0268-8> for estimating and testing large
numbers of effects in many conditions (or many outcomes). Mash takes an
empirical Bayes approach to testing and effect estimation; it estimates
patterns of similarity among conditions, then exploits these patterns to
improve accuracy of the effect estimates. The core linear algebra is
implemented in C++ for fast model fitting and posterior computation.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/code
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
