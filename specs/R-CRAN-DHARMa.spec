%global packname  DHARMa
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Residual Diagnostics for Hierarchical (Multi-Level / Mixed)Regression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-spaMM >= 2.6.0
BuildRequires:    R-CRAN-glmmTMB >= 0.2.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gap 
BuildRequires:    R-CRAN-qrnn 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-spaMM >= 2.6.0
Requires:         R-CRAN-glmmTMB >= 0.2.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gap 
Requires:         R-CRAN-qrnn 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-sfsmisc 
Requires:         R-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-mgcv 

%description
The 'DHARMa' package uses a simulation-based approach to create readily
interpretable scaled (quantile) residuals for fitted (generalized) linear
mixed models. Currently supported are linear and generalized linear
(mixed) models from 'lme4' (classes 'lmerMod', 'glmerMod'), 'glmmTMB' and
'spaMM', generalized additive models ('gam' from 'mgcv'), 'glm' (including
'negbin' from 'MASS', but excluding quasi-distributions) and 'lm' model
classes. Moreover, externally created simulations, e.g. posterior
predictive simulations from Bayesian software such as 'JAGS', 'STAN', or
'BUGS' can be processed as well. The resulting residuals are standardized
to values between 0 and 1 and can be interpreted as intuitively as
residuals from a linear regression. The package also provides a number of
plot and test functions for typical model misspecification problems, such
as over/underdispersion, zero-inflation, and residual spatial and temporal
autocorrelation.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
