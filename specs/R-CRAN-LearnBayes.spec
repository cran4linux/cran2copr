%global __brp_check_rpaths %{nil}
%global packname  LearnBayes
%global packver   2.15.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.15.1
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Learning Bayesian Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of functions helpful in learning the basic tenets of Bayesian
statistical inference.  It contains functions for summarizing basic one
and two parameter posterior distributions and predictive distributions.
It contains MCMC algorithms for summarizing posterior distributions
defined by the user.  It also contains functions for regression models,
hierarchical models, Bayesian tests, and illustrations of Gibbs sampling.

%prep
%setup -q -c -n %{packname}


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
