%global __brp_check_rpaths %{nil}
%global packname  bayesCT
%global packver   0.99.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.3
Release:          2%{?dist}%{?buildtag}
Summary:          Simulation and Analysis of Adaptive Bayesian Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-bayesDP 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-survival 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-bayesDP 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-survival 

%description
Simulation and analysis of Bayesian adaptive clinical trials for binomial,
Gaussian, and time-to-event data types, incorporates historical data and
allows early stopping for futility or early success. The package uses
novel and efficient Monte Carlo methods for estimating Bayesian posterior
probabilities, evaluation of loss to follow up, and imputation of
incomplete data. The package has the functionality for dynamically
incorporating historical data into the analysis via the power prior or
non-informative priors.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
