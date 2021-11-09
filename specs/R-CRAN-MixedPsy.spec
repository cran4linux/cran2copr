%global __brp_check_rpaths %{nil}
%global packname  MixedPsy
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for the Analysis of Psychophysical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-brglm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-ggplot2 

%description
Tools for the analysis of psychophysical data in R. This package allows to
estimate the Point of Subjective Equivalence (PSE) and the Just Noticeable
Difference (JND), either from a psychometric function or from a
Generalized Linear Mixed Model (GLMM). Additionally, the package allows
plotting the fitted models and the response data, simulating psychometric
functions of different shapes, and simulating data sets. For a description
of the use of GLMMs applied to psychophysical data, refer to Moscatelli et
al. (2012).

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
