%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  calms
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Analysis of Latent Means

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-lsr 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-bslib 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-lsr 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-bslib 

%description
Provides a Shiny application to conduct comprehensive analysis of latent
means including the examination of group equivalency, propensity score
analysis, measurement invariance analysis, and assessment of latent mean
differences of equivalent groups with invariant data. Group equivalency
and propensity score analyses are implemented using the 'MatchIt' package
[Ho et al. (2011) <doi:10.18637/jss.v042.i08>], ensuring robust control
for covariates. Structural equation modeling and invariance testing rely
heavily on the 'lavaan' package [Rosseel (2012)
<doi:10.18637/jss.v048.i02>], providing a flexible and powerful modeling
framework. The application also integrates modified functions from
Hammack-Brown et al. (2021) <doi:10.1002/hrdq.21452> to support factor
ratio testing and the list-and-delete procedure.

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
