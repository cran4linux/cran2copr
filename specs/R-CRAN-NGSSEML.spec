%global packname  NGSSEML
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Non-Gaussian State-Space with Exact Marginal Likelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-dlm 
Requires:         R-CRAN-car 
Requires:         R-CRAN-interp 

%description
Due to a large quantity of non-Gaussian time series and reliability data,
the R-package non-Gaussian state-space with exact marginal likelihood is
useful for modeling and forecasting non-Gaussian time series and
reliability data via non-Gaussian state-space models with the exact
marginal likelihood easily, see Gamerman, Santos and Franco (2013)
<doi:10.1111/jtsa.12039> and Santos, Gamerman and Franco (2017)
<doi:10.1109/TR.2017.2670142>. The package gives codes for formulating and
specifying the non-Gaussian state-space models in the R language.
Inferences for the parameters of the model can be made under the classical
and Bayesian. Furthermore, prediction, filtering, and smoothing procedures
can be used to perform inferences for the latent parameters. Applications
include, e.g., count, volatility, piecewise exponential, and software
reliability data.

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
%{rlibdir}/%{packname}/INDEX
