%global packname  automultinomial
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}
Summary:          Models for Spatially Correlated Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Fits the autologistic model described in Besag's famous 1974 paper on
auto- models <http://www.jstor.org/stable/2984812>. Fits a multicategory
generalization of the autologistic model when there are more than 2
response categories. Provides support for both asymptotic and bootstrap
confidence intervals. For full model descriptions and a guide to the use
of this package, please see the vignette.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
