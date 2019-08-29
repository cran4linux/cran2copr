%global packname  eefAnalytics
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Analysing Education Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-metafor 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides tools for analysing education trials. Making different methods
accessible in a single place is essential for sensitivity analysis of
education trials, particularly the implication of the different methods in
analysing simple randomised trials, cluster randomised trials and
multisite trials.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
