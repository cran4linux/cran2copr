%global packname  NetMix
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Dynamic Mixed-Membership Network Regression Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-graphics >= 3.5.2
BuildRequires:    R-grDevices >= 3.5.2
BuildRequires:    R-methods >= 3.5.2
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-utils >= 3.5.2
BuildRequires:    R-CRAN-lda >= 1.4.2
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-Matrix >= 1.2.15
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-poisbinom >= 1.0.1
BuildRequires:    R-CRAN-clue >= 0.3.54
BuildRequires:    R-CRAN-RSpectra >= 0.14.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3.51.4
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-graphics >= 3.5.2
Requires:         R-grDevices >= 3.5.2
Requires:         R-methods >= 3.5.2
Requires:         R-stats >= 3.5.2
Requires:         R-utils >= 3.5.2
Requires:         R-CRAN-lda >= 1.4.2
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-Matrix >= 1.2.15
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-poisbinom >= 1.0.1
Requires:         R-CRAN-clue >= 0.3.54
Requires:         R-CRAN-RSpectra >= 0.14.0

%description
Variational EM estimation of mixed-membership stochastic blockmodel for
networks, incorporating node-level predictors of mixed-membership vectors,
as well as dyad-level predictors. For networks observed over time, the
model defines a hidden Markov process that allows the effects of
node-level predictors to evolve in discrete, historical periods. In
addition, the package offers a variety of utilities for exploring results
of estimation, including tools for conducting posterior predictive checks
of goodness-of-fit and several plotting functions. The package implements
methods described in Olivella, Pratt and Imai (2019) ``Dynamic Stochastic
Blockmodel Regression for Social Networks: Application to International
Conflicts'', available at
<http://santiagoolivella.info/wp-content/uploads/2018/07/dSBM_Reg.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
