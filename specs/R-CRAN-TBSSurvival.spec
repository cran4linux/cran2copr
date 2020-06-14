%global packname  TBSSurvival
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Survival Analysis using a Transform-Both-Sides Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-normalp 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-BMS 
Requires:         R-CRAN-normalp 
Requires:         R-survival 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-BMS 

%description
Functions to perform the reliability/survival analysis using a parametric
Transform-both-sides (TBS) model.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
