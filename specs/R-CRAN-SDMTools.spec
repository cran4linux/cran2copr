%global packname  SDMTools
%global packver   1.1-221.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.221.1
Release:          1%{?dist}
Summary:          Species Distribution Modelling Tools: Tools for processing dataassociated with species distribution modelling exercises

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-R.utils 

%description
This packages provides a set of tools for post processing the outcomes of
species distribution modeling exercises. It includes novel methods for
comparing models and tracking changes in distributions through time. It
further includes methods for visualizing outcomes, selecting thresholds,
calculating measures of accuracy and landscape fragmentation statistics,
etc.. This package was made possible in part by financial support from the
Australian Research Council & ARC Research Network for Earth System
Science.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
