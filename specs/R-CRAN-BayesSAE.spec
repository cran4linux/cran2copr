%global packname  BayesSAE
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Bayesian Analysis of Small Area Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-coda 
Requires:         R-lattice 

%description
Provides a variety of methods from Rao (2003, ISBN:0-471-41374-7) and some
other research articles to deal with several specific small area area-
level models in Bayesian framework. Models provided range from the basic
Fay-Herriot model to its improvement such as You-Chapman models, unmatched
models, spatial models and so on. Different types of priors for specific
parameters could be chosen to obtain MCMC posterior draws. The main
sampling function is written in C with GSL lab so as to facilitate the
computation. Model internal checking and model comparison criteria are
also involved.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
