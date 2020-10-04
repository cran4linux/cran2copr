%global packname  serrsBayes
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Modelling of Raman Spectroscopy

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-Matrix 
Requires:         R-CRAN-truncnorm 
Requires:         R-splines 
Requires:         R-methods 

%description
Sequential Monte Carlo (SMC) algorithms for fitting a generalised additive
mixed model (GAMM) to surface-enhanced resonance Raman spectroscopy
(SERRS), using the method of Moores et al. (2016) <arXiv:1604.07299>.
Multivariate observations of SERRS are highly collinear and lend
themselves to a reduced-rank representation. The GAMM separates the SERRS
signal into three components: a sequence of Lorentzian, Gaussian, or
pseudo-Voigt peaks; a smoothly-varying baseline; and additive white noise.
The parameters of each component of the model are estimated iteratively
using SMC. The posterior distributions of the parameters given the
observed spectra are represented as a population of weighted particles.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
