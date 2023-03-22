%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  missingHE
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Missing Outcome Data in Health Economic Evaluation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mcmcplots 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggmcmc 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-BCEA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mcmcr 
Requires:         R-CRAN-mcmcplots 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggmcmc 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-BCEA 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-bayesplot 
Requires:         R-methods 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mcmcr 

%description
Contains a suite of functions for health economic evaluations with missing
outcome data. The package can fit different types of statistical models
under a fully Bayesian approach using the software 'JAGS' (which should be
installed locally and which is loaded in 'missingHE' via the 'R' package
'R2jags'). Three classes of models can be fitted under a variety of
missing data assumptions: selection models, pattern mixture models and
hurdle models. In addition to model fitting, 'missingHE' provides a set of
specialised functions to assess model convergence and fit, and to
summarise the statistical and economic results using different types of
measures and graphs. The methods implemented are described in Mason (2018)
<doi:10.1002/hec.3793>, Molenberghs (2000)
<doi:10.1007/978-1-4419-0300-6_18> and Gabrio (2019)
<doi:10.1002/sim.8045>.

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
