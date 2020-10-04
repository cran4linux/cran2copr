%global packname  swissMrP
%global packver   0.62
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.62
Release:          3%{?dist}%{?buildtag}
Summary:          Multilevel Regression with Post-Stratification (MrP) forSwitzerland

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-blme 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-blme 
Requires:         R-CRAN-sp 
Requires:         R-utils 

%description
Provides a number of useful functions to employ MrP for small area
prediction in Switzerland. Based on a hierarchical model and survey data
one can derive cantonal preference measures. The package allows to
automatize the prediction and post-stratification steps. It further
provides adequate print, summary, map, and plot functions for objects of
its class.

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
