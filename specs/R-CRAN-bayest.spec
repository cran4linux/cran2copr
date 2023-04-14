%global __brp_check_rpaths %{nil}
%global packname  bayest
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Effect Size Targeted Bayesian Two-Sample t-Tests via MarkovChain Monte Carlo in Gaussian Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-MCMCpack 

%description
Provides an Markov-Chain-Monte-Carlo algorithm for Bayesian t-tests on the
effect size. The underlying Gibbs sampler is based on a two-component
Gaussian mixture and approximates the posterior distributions of the
effect size, the difference of means and difference of standard
deviations. A posterior analysis of the effect size via the region of
practical equivalence is provided, too. For more details about the Gibbs
sampler see Kelter (2019) <arXiv:1906.07524>.

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
