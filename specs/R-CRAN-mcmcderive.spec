%global packname  mcmcderive
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Derive MCMC Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-err 
BuildRequires:    R-CRAN-checkr 
BuildRequires:    R-CRAN-mcmcr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-err 
Requires:         R-CRAN-checkr 
Requires:         R-CRAN-mcmcr 
Requires:         R-CRAN-purrr 

%description
Generates derived parameter(s) from Monte Carlo Markov Chain (MCMC)
samples using R code. This allows Bayesian models to be fitted without the
inclusion of derived parameters which add unnecessary clutter and slow
model fitting. For more information on MCMC samples see Brooks et al.
(2011) <isbn:978-1-4200-7941-8>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
