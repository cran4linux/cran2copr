%global packname  mgpd
%global packver   1.99
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.99
Release:          1%{?dist}
Summary:          mgpd: Functions for multivariate generalized Pareto distribution(MGPD of Type II)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-fields 

%description
Extends distribution and density functions to parametric multivariate
generalized Pareto distributions (MGPD of Type II), and provides fitting
functions which calculate maximum likelihood estimates for bivariate and
trivariate models. (Help is under progress)

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
