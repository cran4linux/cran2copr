%global packname  bamp
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          3%{?dist}
Summary:          Bayesian Age-Period-Cohort Modeling and Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-abind 

%description
Bayesian Age-Period-Cohort Modeling and Prediction using efficient Markov
Chain Monte Carlo Methods. This is the R version of the previous BAMP
software as described in Volker Schmid and Leonhard Held (2007)
<DOI:10.18637/jss.v021.i08> Bayesian Age-Period-Cohort Modeling and
Prediction - BAMP, Journal of Statistical Software 21:8. This package
includes checks of convergence using Gelman's R.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
