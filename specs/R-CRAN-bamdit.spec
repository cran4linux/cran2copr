%global packname  bamdit
%global packver   3.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.2
Release:          3%{?dist}
Summary:          Bayesian Meta-Analysis of Diagnostic Test Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-rjags >= 3.4
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggExtra >= 0.8
BuildRequires:    R-CRAN-R2jags >= 0.04.03
BuildRequires:    R-grid 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-rjags >= 3.4
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggExtra >= 0.8
Requires:         R-CRAN-R2jags >= 0.04.03
Requires:         R-grid 

%description
Functions for Bayesian meta-analysis of diagnostic test data which are
based on a scale mixtures bivariate random-effects model.

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
