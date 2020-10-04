%global packname  spate
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Modeling of Large Data Using a Spectral SPDEApproach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
Requires:         fftw
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 

%description
Functionality for spatio-temporal modeling of large data sets is provided.
A Gaussian process in space and time is defined through a stochastic
partial differential equation (SPDE). The SPDE is solved in the spectral
space, and after discretizing in time and space, a linear Gaussian state
space model is obtained. When doing inference, the main computational
difficulty consists in evaluating the likelihood and in sampling from the
full conditional of the spectral coefficients, or equivalently, the latent
space-time process. In comparison to the traditional approach of using a
spatio-temporal covariance function, the spectral SPDE approach is
computationally advantageous. See Sigrist, Kuensch, and Stahel (2015)
<doi:10.1111/rssb.12061> for more information on the methodology. This
package aims at providing tools for two different modeling approaches.
First, the SPDE based spatio-temporal model can be used as a component in
a customized hierarchical Bayesian model (HBM). The functions of the
package then provide parameterizations of the process part of the model as
well as computationally efficient algorithms needed for doing inference
with the HBM. Alternatively, the adaptive MCMC algorithm implemented in
the package can be used as an algorithm for doing inference without any
additional modeling. The MCMC algorithm supports data that follow a
Gaussian or a censored distribution with point mass at zero. Covariates
can be included in the model through a regression term.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
