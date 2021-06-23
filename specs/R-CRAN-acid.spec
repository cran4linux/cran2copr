%global __brp_check_rpaths %{nil}
%global packname  acid
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Analysing Conditional Income Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-datasets 
BuildRequires:    R-methods 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-datasets 
Requires:         R-methods 

%description
Functions for the analysis of income distributions for subgroups of the
population as defined by a set of variables like age, gender, region, etc.
This entails a Kolmogorov-Smirnov test for a mixture distribution as well
as functions for moments, inequality measures, entropy measures and
polarisation measures of income distributions. This package thus aides the
analysis of income inequality by offering tools for the exploratory
analysis of income distributions at the disaggregated level.

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
