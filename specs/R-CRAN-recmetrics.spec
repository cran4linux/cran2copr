%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  recmetrics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Psychometric Evaluation Using Relative Excess Correlations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 

%description
Modern results of psychometric theory are implemented to provide users
with a way of evaluating the internal structure of a set of items guided
by theory. These methods are discussed in detail in VanderWeele and
Padgett (2024) <doi:10.31234/osf.io/rnbk5>. The relative excess
correlation matrices will, generally, have numerous negative entries even
if all of the raw correlations between each pair of indicators are
positive. The positive deviations of the relative excess correlation
matrix entries help identify clusters of indicators that are more strongly
related to one another, providing insights somewhat analogous to factor
analysis, but without the need for rotations or decisions concerning the
number of factors. A goal similar to exploratory/confirmatory factor
analysis, but 'recmetrics' uses novel methods that do not rely on
assumptions of latent variables or latent variable structures.

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
