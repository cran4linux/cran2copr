%global packname  miWQS
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation Using Weighted Quantile Sum Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.49
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-CRAN-survival >= 3.1.12
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-condMVNorm >= 2015.2
BuildRequires:    R-CRAN-MCMCpack >= 1.4.4
BuildRequires:    R-CRAN-tmvtnorm >= 1.4.10
BuildRequires:    R-CRAN-glm2 >= 1.2.1
BuildRequires:    R-CRAN-Rsolnp >= 1.16
BuildRequires:    R-CRAN-invgamma >= 1.1
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-tmvmixnorm >= 1.0.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0.10
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-matrixNormal >= 0.0.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.49
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-CRAN-survival >= 3.1.12
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-condMVNorm >= 2015.2
Requires:         R-CRAN-MCMCpack >= 1.4.4
Requires:         R-CRAN-tmvtnorm >= 1.4.10
Requires:         R-CRAN-glm2 >= 1.2.1
Requires:         R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-invgamma >= 1.1
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-tmvmixnorm >= 1.0.2
Requires:         R-CRAN-mvtnorm >= 1.0.10
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-matrixNormal >= 0.0.0
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
The `miWQS` package handles the uncertainty due to below the detection
limit in a correlated component mixture problem.  Researchers want to
determine if a set/mixture of continuous and correlated
components/chemicals is associated with an outcome and if so, which
components are important in that mixture. These components share a common
outcome but are interval-censored between zero and low thresholds, or
detection limits, that may be different across the components. The `miWQS`
package applies the multiple imputation (MI) procedure to the weighted
quantile sum regression (WQS) methodology for continuous, binary, or count
outcomes (Hargarten & Wheeler (2020) <doi:10.1016/j.envres.2020.109466>).
The imputation models are: bootstrapping imputation (Lubin et.al (2004)
<doi:10.1289/ehp.7199>), univariate Bayesian imputation (Hargarten &
Wheeler (2020) <doi:10.1016/j.envres.2020.109466>), and multivariate
Bayesian regression imputation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
