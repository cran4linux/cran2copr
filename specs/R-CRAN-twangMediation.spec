%global __brp_check_rpaths %{nil}
%global packname  twangMediation
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Twang Causal Mediation Modeling via Weighting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gbm >= 1.5.3
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-gbm >= 1.5.3
Requires:         R-CRAN-twang 
Requires:         R-CRAN-gridExtra 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-survey 

%description
Provides functions for estimating natural direct and indirect effects for
mediation analysis. It uses weighting where the weights are functions of
estimates of the probability of exposure or treatment assignment (Hong, G
(2010).
<https://cepa.stanford.edu/sites/default/files/workshops/GH_JSM%%20Proceedings%%202010.pdf>
Huber, M. (2014). <doi:10.1002/jae.2341>). Estimation of probabilities can
use generalized boosting or logistic regression. Additional functions
provide diagnostics of the model fit and weights. The vignette provides
details and examples.

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
