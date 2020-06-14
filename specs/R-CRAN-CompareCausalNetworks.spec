%global packname  CompareCausalNetworks
%global packver   0.2.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6.2
Release:          2%{?dist}
Summary:          Interface to Diverse Estimation Methods of Causal Networks

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-data.table 

%description
Unified interface for the estimation of causal networks, including the
methods 'backShift' (from package 'backShift'), 'bivariateANM' (bivariate
additive noise model), 'bivariateCAM' (bivariate causal additive model),
'CAM' (causal additive model) (from package 'CAM'; the package is
temporarily unavailable on the CRAN repository; formerly available
versions can be obtained from the archive), 'hiddenICP' (invariant causal
prediction with hidden variables), 'ICP' (invariant causal prediction)
(from package 'InvariantCausalPrediction'), 'GES' (greedy equivalence
search), 'GIES' (greedy interventional equivalence search), 'LINGAM', 'PC'
(PC Algorithm), 'FCI' (fast causal inference), 'RFCI' (really fast causal
inference) (all from package 'pcalg') and regression.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
