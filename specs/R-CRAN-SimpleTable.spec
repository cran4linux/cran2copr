%global packname  SimpleTable
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Bayesian Inference and Sensitivity Analysis for Causal Effectsfrom 2 x 2 and 2 x 2 x K Tables in the Presence of UnmeasuredConfounding

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.1
Requires:         R-core >= 2.5.1
BuildArch:        noarch
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-hdrcde 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-MCMCpack 
Requires:         R-tcltk 

%description
SimpleTable provides a series of methods to conduct Bayesian inference and
sensitivity analysis for causal effects from 2 x 2 and 2 x 2 x K tables
when unmeasured confounding is present or suspected.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
