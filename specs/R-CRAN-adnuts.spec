%global packname  adnuts
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          No-U-Turn MCMC Sampling for 'ADMB' and 'TMB' Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-R2admb 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-R2admb 

%description
Bayesian inference using the no-U-turn (NUTS) algorithm by Hoffman and
Gelman (2014) <http://www.jmlr.org/papers/v15/hoffman14a.html>. Designed
for 'AD Model Builder' ('ADMB') models, or when R functions for
log-density and log-density gradient are available, such as 'Template
Model Builder' ('TMB') models and other special cases. Functionality is
similar to 'Stan', and the 'rstan' and 'shinystan' packages are used for
diagnostics and inference.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/demo.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
