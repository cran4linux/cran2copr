%global __brp_check_rpaths %{nil}
%global packname  BSagri
%global packver   0.1-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          3%{?dist}%{?buildtag}
Summary:          Safety Assessment in Agricultural Field Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-MCPAN 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-mratios 
BuildRequires:    R-stats 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-MCPAN 
Requires:         R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-mratios 
Requires:         R-stats 

%description
Collection of functions, data sets and code examples for evaluations of
field trials with the objective of equivalence assessment.

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
