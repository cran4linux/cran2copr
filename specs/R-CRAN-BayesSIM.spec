%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesSIM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integrated Interface of Bayesian Single Index Models using 'nimble'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 

%description
Provides tools for fitting Bayesian single index models with flexible
choices of priors for both the index and the link function. The package
implements model estimation and posterior inference using efficient MCMC
algorithms built on the 'nimble' framework, allowing users to specify,
extend, and simulate models in a unified and reproducible manner. The
following methods are implemented in the package: Antoniadis et al. (2004)
<https://www.jstor.org/stable/24307224>, Wang (2009)
<doi:10.1016/j.csda.2008.12.010>, Choi et al. (2011)
<doi:10.1080/10485251003768019>, Dhara et al. (2019)
<doi:10.1214/19-BA1170>, McGee et al. (2023) <doi:10.1111/biom.13569>.

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
