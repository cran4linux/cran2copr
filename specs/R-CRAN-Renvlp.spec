%global packname  Renvlp
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          3%{?dist}
Summary:          Computing Envelope Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 

%description
Provides a general routine, envMU, which allows estimation of the M
envelope of span(U) given root n consistent estimators of M and U. The
routine envMU does not presume a model.  This package implements response
envelopes, partial response envelopes, envelopes in the predictor space,
heteroscedastic envelopes, simultaneous envelopes, scaled response
envelopes, scaled envelopes in the predictor space, groupwise envelopes,
weighted envelopes, envelopes in logistic regression and envelopes in
Poisson regression. For each of these model-based routines the package
provides inference tools including bootstrap, cross validation, estimation
and prediction, hypothesis testing on coefficients are included except for
weighted envelopes. Tools for selection of dimension include AIC, BIC and
likelihood ratio testing.  Background is available at Cook, R. D.,
Forzani, L. and Su, Z. (2016) <doi:10.1016/j.jmva.2016.05.006>.
Optimization is based on a clockwise coordinate descent algorithm.

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
