%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlmoderator
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probing, Plotting, and Interpreting Multilevel Interaction Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 

%description
Provides a unified workflow for probing, plotting, and assessing the
robustness of cross-level interaction effects in two-level mixed-effects
models fitted with 'lme4' (Bates et al., 2015)
<doi:10.18637/jss.v067.i01>. Implements simple slopes analysis following
Aiken and West (1991, ISBN:9780761907121), Johnson-Neyman intervals
following Johnson and Fay (1950) <doi:10.1007/BF02288864> and Bauer and
Curran (2005) <doi:10.1207/s15327906mbr4003_5>, and grand- or group-mean
centering as described in Enders and Tofighi (2007)
<doi:10.1037/1082-989X.12.2.121>. Includes a slope variance decomposition
that separates fixed-effect uncertainty from random-slope variance
(tau11), a contour surface plot of predicted outcomes over the full
predictor-by-moderator space, and robustness diagnostics comprising
intraclass correlation coefficient shift analysis and
leave-one-cluster-out (LOCO) stability checks. Designed for researchers in
education, psychology, biostatistics, epidemiology, organizational
science, and other fields where outcomes are clustered within higher-level
units.

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
