%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crmPack
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Object-Oriented Implementation of Dose Escalation Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-checkmate >= 2.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-checkmate >= 2.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Implements a wide range of dose escalation designs. The focus is on
model-based designs, ranging from classical and modern continual
reassessment methods (CRMs) based on dose-limiting toxicity endpoints to
dual-endpoint designs taking into account a biomarker/efficacy outcome.
Bayesian inference is performed via MCMC sampling in JAGS, and it is easy
to setup a new design with custom JAGS code. However, it is also possible
to implement 3+3 designs for comparison or models with non-Bayesian
estimation. The whole package is written in a modular form in the S4 class
system, making it very flexible for adaptation to new models, escalation
or stopping rules. Further details are presented in Sabanes Bove et al.
(2019) <doi:10.18637/jss.v089.i10>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
