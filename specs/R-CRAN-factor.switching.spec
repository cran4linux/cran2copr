%global packname  factor.switching
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Post-Processing MCMC Outputs of Bayesian Factor Analytic Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-lpSolve 

%description
A well known identifiability issue in factor analytic models is the
invariance with respect to orthogonal transformations. This problem
burdens the inference under a Bayesian setup, where Markov chain Monte
Carlo (MCMC) methods are used to generate samples from the posterior
distribution. The package applies a series of rotation, sign and
permutation transformations into raw MCMC samples of factor loadings,
which are provided by the user. The post-processed output is identifiable
and can be used for MCMC inference on any parametric function of factor
loadings. Comparison of multiple MCMC chains is also possible.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
