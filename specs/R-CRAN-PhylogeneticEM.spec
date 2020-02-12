%global packname  PhylogeneticEM
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Automatic Shift Detection using a Phylogenetic EM

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-graphics >= 3.6.0
BuildRequires:    R-grDevices >= 3.6.0
BuildRequires:    R-methods >= 3.6.0
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-utils >= 3.6.0
BuildRequires:    R-CRAN-glmnet >= 2.0.5
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-gglasso >= 1.4
BuildRequires:    R-Matrix >= 1.2.3
BuildRequires:    R-CRAN-capushe >= 1.1.1
BuildRequires:    R-CRAN-LINselect >= 1.1.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-robustbase >= 0.92.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-ape >= 5.3
Requires:         R-graphics >= 3.6.0
Requires:         R-grDevices >= 3.6.0
Requires:         R-methods >= 3.6.0
Requires:         R-stats >= 3.6.0
Requires:         R-utils >= 3.6.0
Requires:         R-CRAN-glmnet >= 2.0.5
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-gglasso >= 1.4
Requires:         R-Matrix >= 1.2.3
Requires:         R-CRAN-capushe >= 1.1.1
Requires:         R-CRAN-LINselect >= 1.1.1
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-robustbase >= 0.92.6

%description
Implementation of the automatic shift detection method for Brownian Motion
(BM) or Ornstein–Uhlenbeck (OU) models of trait evolution on phylogenies.
Some tools to handle equivalent shifts configurations are also available.
See Bastide et al. (2017) <doi:10.1111/rssb.12206> and Bastide et al.
(2018) <doi:10.1093/sysbio/syy005>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
