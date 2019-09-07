%global packname  slm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Stationary Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-capushe 
Requires:         R-CRAN-ltsa 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-capushe 

%description
Provides statistical procedures for linear regression in the general
context where the errors are assumed to be correlated. Different ways to
estimate the asymptotic covariance matrix of the least squares estimators
are available. Starting from this estimation of the covariance matrix, the
confidence intervals and the usual tests on the parameters are modified.
The functions of this package are very similar to those of 'lm': it
contains methods such as summary(), plot(), confint() and predict(). The
'slm' package is described in the paper by E. Caron, J. Dedecker and B.
Michel (2019), "Linear regression with stationary errors: the R package
slm", arXiv preprint <arXiv:1906.06583>.

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
%{rlibdir}/%{packname}/INDEX
