%global packname  sns
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Newton Sampler (SNS)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-numDeriv 

%description
Stochastic Newton Sampler (SNS) is a Metropolis-Hastings-based, Markov
Chain Monte Carlo sampler for twice differentiable, log-concave
probability density functions (PDFs) where the proposal density function
is a multivariate Gaussian resulting from a second-order Taylor-series
expansion of log-density around the current point. The mean of the
Gaussian proposal is the full Newton-Raphson step from the current point.
A Boolean flag allows for switching from SNS to Newton-Raphson
optimization (by choosing the mean of proposal function as next point).
This can be used during burn-in to get close to the mode of the PDF (which
is unique due to concavity). For high-dimensional densities, mixing can be
improved via 'state space partitioning' strategy, in which SNS is applied
to disjoint subsets of state space, wrapped in a Gibbs cycle. Numerical
differentiation is available when analytical expressions for gradient and
Hessian are not available. Facilities for validation and numerical
differentiation of log-density are provided.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
