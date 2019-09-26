%global packname  BayesMallows
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Bayesian Preference Learning with the Mallows Rank Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-PerMallows >= 1.13
BuildRequires:    R-CRAN-sets >= 1.0.18
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 0.9.3
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-Rdpack >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-relations >= 0.6.8
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-HDInterval >= 0.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-PerMallows >= 1.13
Requires:         R-CRAN-sets >= 1.0.18
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-cowplot >= 0.9.3
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-Rdpack >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-relations >= 0.6.8
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-HDInterval >= 0.2.0
Requires:         R-stats 

%description
An implementation of the Bayesian version of the Mallows rank model
(Vitelli et al., Journal of Machine Learning Research, 2018
<http://jmlr.org/papers/v18/15-481.html>; Crispino et al., to appear in
Annals of Applied Statistics). Both Cayley, footrule, Hamming, Kendall,
Spearman, and Ulam distances are supported in the models. The rank data to
be analyzed can be in the form of complete rankings, top-k rankings,
partially missing rankings, as well as consistent and inconsistent
pairwise preferences. Several functions for plotting and studying the
posterior distributions of parameters are provided. The package also
provides functions for estimating the partition function (normalizing
constant) of the Mallows rank model, both with the importance sampling
algorithm of Vitelli et al. and asymptotic approximation with the IPFP
algorithm (Mukherjee, Annals of Statistics, 2016
<doi:10.1214/15-AOS1389>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
