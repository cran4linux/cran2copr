%global __brp_check_rpaths %{nil}
%global packname  RBesT
%global packver   1.6-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          R Bayesian Evidence Synthesis Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-CRAN-rstantools,make
Requires:         R-CRAN-rstantools,pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.19.2
BuildRequires:    R-CRAN-StanHeaders >= 2.19.0
BuildRequires:    R-CRAN-BH >= 1.69.0
BuildRequires:    R-CRAN-bayesplot >= 1.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rstan >= 2.19.2
Requires:         R-CRAN-bayesplot >= 1.4.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Tool-set to support Bayesian evidence synthesis.  This includes
meta-analysis, (robust) prior derivation from historical data, operating
characteristics and analysis (1 and 2 sample cases). Please refer to
Neuenschwander et al. (2010) <doi:10.1177/1740774509356002> and Schmidli
et al. (2014) <doi:10.1111/biom.12242> for details on the methodology.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/sbc
%doc %{rlibdir}/%{packname}/stan
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
