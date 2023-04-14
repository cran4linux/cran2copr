%global __brp_check_rpaths %{nil}
%global packname  Immigrate
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Iterative Max-Min Entropy Margin-Maximization with InteractionTerms for Feature Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pROC 
Requires:         R-stats 

%description
Based on large margin principle, this package performs feature selection
methods: "IM4E"(Iterative Margin-Maximization under Max-Min Entropy
Algorithm); "Immigrate"(Iterative Max-Min Entropy Margin-Maximization with
Interaction Terms Algorithm); "BIM"(Boosted version of IMMIGRATE
algorithm); "Simba"(Iterative Search Margin Based Algorithm); "LFE"(Local
Feature Extraction Algorithm). This package also performs prediction for
the above feature selection methods.

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
%{rlibdir}/%{packname}
