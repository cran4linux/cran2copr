%global __brp_check_rpaths %{nil}
%global packname  MultiRR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bias, Precision, and Power for Multi-Level Random Regressions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-CRAN-lme4 

%description
Calculates bias, precision, and power for multi-level random regressions.
Random regressions are types of hierarchical models in which data are
structured in groups and (regression) coefficients can vary by groups.
Tools to estimate model performance are designed mostly for scenarios
where (regression) coefficients vary at just one level. 'MultiRR' provides
simulation and analytical tools (based on 'lme4') to study model
performance for random regressions that vary at more than one level
(multi-level random regressions), allowing researchers to determine
optimal sampling designs.

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
