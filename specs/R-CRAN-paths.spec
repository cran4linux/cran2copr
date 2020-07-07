%global packname  paths
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          An Imputation Approach to Estimating Path-Specific CausalEffects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-BART 
Requires:         R-boot 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metR 
Requires:         R-parallel 
Requires:         R-CRAN-pryr 
Requires:         R-stats 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-tidyr 

%description
In causal mediation analysis with multiple causally ordered mediators, a
set of path-specific effects are identified under standard ignorability
assumptions. This package implements an imputation approach to estimating
these effects along with a set of bias formulas for conducting sensitivity
analysis (Zhou and Yamamoto <doi:10.31235/osf.io/2rx6p>). It contains two
main functions: paths() for estimating path-specific effects and sens()
for conducting sensitivity analysis. Estimation uncertainty is quantified
using the nonparametric bootstrap.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
