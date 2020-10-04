%global packname  idem
%global packver   5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Inference in Randomized Controlled Trials with Death andMissingness

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-mice >= 3.9.0
BuildRequires:    R-parallel >= 3.2
BuildRequires:    R-survival >= 2.38
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.0
BuildRequires:    R-CRAN-sqldf >= 0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
Requires:         R-CRAN-mice >= 3.9.0
Requires:         R-parallel >= 3.2
Requires:         R-survival >= 2.38
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 1.5.0
Requires:         R-CRAN-sqldf >= 0.4
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 

%description
In randomized studies involving severely ill patients, functional outcomes
are often unobserved due to missed clinic visits, premature withdrawal or
death. It is well known that if these unobserved functional outcomes are
not handled properly, biased treatment comparisons can be produced. In
this package, we implement a procedure for comparing treatments that is
based on the composite endpoint of both the functional outcome and
survival. The procedure was proposed in Wang et al. (2016)
<DOI:10.1111/biom.12594> and Wang et al. (2020)
<DOI:10.18637/jss.v093.i12>. It considers missing data imputation with
different sensitivity analysis strategies to handle the unobserved
functional outcomes not due to death.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
