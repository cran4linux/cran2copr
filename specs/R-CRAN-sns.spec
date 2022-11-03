%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sns
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
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
differentiation of log-density are provided. Note: Formerly available
versions of the MfUSampler can be obtained from the archive
<https://cran.r-project.org/src/contrib/Archive/MfUSampler/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
