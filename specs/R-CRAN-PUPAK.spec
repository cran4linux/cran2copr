%global __brp_check_rpaths %{nil}
%global packname  PUPAK
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Estimation, and Plot Visualization of Adsorption Kinetic Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-segmented 
Requires:         R-stats 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-segmented 

%description
Contains model fitting functions for linear and non-linear adsorption
kinetic and diffusion models. Adsorption kinetics is used for
characterizing the rate of solute adsorption and the time necessary for
the adsorption process. Adsorption kinetics offers vital information on
adsorption rate, adsorbent performance in response time, and mass transfer
processes. In addition, diffusion models are included in the package as
solute diffusion affects the adsorption kinetic experiments. This package
consists of 20 adsorption and diffusion models, including Pseudo First
Order (PFO), Pseudo Second Order (PSO), Elovich, and Weber-Morris model
(commonly called the intraparticle model) stated by Plazinski et al.
(2009) <doi:10.1016/j.cis.2009.07.009>. This package also contains a
summary function where the statistical errors of each model are ranked for
a more straightforward determination of the best fit model.

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
