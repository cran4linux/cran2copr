%global packname  wfe
%global packver   1.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.1
Release:          2%{?dist}
Summary:          Weighted Linear Fixed Effects Regression Models for CausalInference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-utils 
Requires:         R-CRAN-arm 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-methods 

%description
Provides a computationally efficient way of fitting weighted linear fixed
effects estimators for causal inference with various weighting schemes.
Weighted linear fixed effects estimators can be used to estimate the
average treatment effects under different identification strategies. This
includes stratified randomized experiments, matching and stratification
for observational studies, first differencing, and
difference-in-differences. The package implements methods described in
Imai and Kim (2017) "When should We Use Linear Fixed Effects Regression
Models for Causal Inference with Longitudinal Data?", available at
<https://imai.fas.harvard.edu/research/FEmatch.html>.

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
