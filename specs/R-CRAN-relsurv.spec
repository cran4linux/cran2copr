%global packname  relsurv
%global packver   2.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Relative Survival

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-survival >= 2.42
BuildRequires:    R-CRAN-date 
BuildRequires:    R-splines 
Requires:         R-survival >= 2.42
Requires:         R-CRAN-date 
Requires:         R-splines 

%description
Contains functions for analysing relative survival data, including
nonparametric estimators of net (marginal relative) survival, relative
survival ratio, crude mortality, methods for fitting and checking additive
and multiplicative regression models, transformation approach, methods for
dealing with population mortality tables.

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
%doc %{rlibdir}/%{packname}/news.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
