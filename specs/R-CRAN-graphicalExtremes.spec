%global packname  graphicalExtremes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Statistical Methodology for Graphical Extreme Value Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-grDevices >= 3.6.0
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats >= 3.6.0
Requires:         R-grDevices >= 3.6.0
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-CRAN-Rdpack 

%description
Statistical methodology for sparse multivariate extreme value models.
Methods are provided for exact simulation and statistical inference for
multivariate Pareto distributions on graphical structures as described in
the paper 'Graphical Models for Extremes' by Engelke and Hitz (2018)
<arXiv:1812.01734>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
