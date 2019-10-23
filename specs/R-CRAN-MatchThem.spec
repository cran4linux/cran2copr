%global packname  MatchThem
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Matching Multiply Imputed Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MatchIt 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-WeightIt 
Requires:         R-stats 

%description
Provides the necessary tools for the pre-processing technique of matching
in multiply imputed datasets, to improve the robustness and transparency
of deriving causal inferences from studying these datasets. This package
includes functions to perform propensity score matching within or across
the imputed datasets as well as to estimate weights (including inverse
propensity score weights) of observations, to analyze each matched or
weighted datasets using parametric or non-parametric statistical models,
and to combine the obtained results from these models according to Rubin’s
rules. Please see the package repository
<https://github.com/FarhadPishgar/MatchThem> for details.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
