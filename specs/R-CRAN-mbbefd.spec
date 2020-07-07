%global packname  mbbefd
%global packver   0.8.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.8.5
Release:          3%{?dist}
Summary:          Maxwell Boltzmann Bose Einstein Fermi Dirac Distribution andDestruction Rate Modelling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-fitdistrplus >= 1.0.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-MASS 
Requires:         R-CRAN-fitdistrplus >= 1.0.7
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-alabama 
Requires:         R-utils 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-gsl 
Requires:         R-MASS 

%description
Distributions that are typically used for exposure rating in general
insurance, in particular to price reinsurance contracts. The vignettes
show code snippets to fit the distribution to empirical data.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
