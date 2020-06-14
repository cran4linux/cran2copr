%global packname  rstan
%global packver   2.19.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.19.3
Release:          2%{?dist}
Summary:          R Interface to Stan

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
Requires:         pandoc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-StanHeaders > 2.18.1
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-pkgbuild 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-StanHeaders > 2.18.1
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-pkgbuild 

%description
User-facing R functions are provided to parse, compile, test, estimate,
and analyze Stan models by accessing the header-only Stan library provided
by the 'StanHeaders' package. The Stan project develops a probabilistic
programming language that implements full Bayesian statistical inference
via Markov Chain Monte Carlo, rough Bayesian inference via 'variational'
approximation, and (optionally penalized) maximum likelihood estimation
via optimization. In all three cases, automatic differentiation is used to
quickly and accurately evaluate gradients without burdening the user with
the need to derive the partial derivatives.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/misc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
