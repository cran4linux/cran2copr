%global packname  hdm
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          High-Dimensional Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Formula 
Requires:         R-methods 

%description
Implementation of selected high-dimensional statistical and econometric
methods for estimation and inference. Efficient estimators and uniformly
valid confidence intervals for various low-dimensional causal/ structural
parameters are provided which appear in high-dimensional approximately
sparse models. Including functions for fitting heteroscedastic robust
Lasso regressions with non-Gaussian errors and for instrumental variable
(IV) and treatment effect estimation in a high-dimensional setting.
Moreover, the methods enable valid post-selection inference and rely on a
theoretically grounded, data-driven choice of the penalty. Chernozhukov,
Hansen, Spindler (2016) <arXiv:1603.01700>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
