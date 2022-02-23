%global __brp_check_rpaths %{nil}
%global packname  bfw
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Framework for Computational Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-runjags >= 2.0.4.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-circlize >= 0.4.4
BuildRequires:    R-CRAN-officer >= 0.3.1
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-CRAN-rvg >= 0.1.9
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-runjags >= 2.0.4.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-circlize >= 0.4.4
Requires:         R-CRAN-officer >= 0.3.1
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-rvg >= 0.1.9
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Derived from the work of Kruschke (2015, <ISBN:9780124058880>), the
present package aims to provide a framework for conducting Bayesian
analysis using Markov chain Monte Carlo (MCMC) sampling utilizing the Just
Another Gibbs Sampler ('JAGS', Plummer, 2003,
<https://mcmc-jags.sourceforge.io>).  The initial version includes several
modules for conducting Bayesian equivalents of chi-squared tests, analysis
of variance (ANOVA), multiple (hierarchical) regression, softmax
regression, and for fitting data (e.g., structural equation modeling).

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
