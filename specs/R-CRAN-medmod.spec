%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  medmod
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Mediation and Moderation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-jmvcore >= 1.0.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-jmvcore >= 1.0.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-rlang 

%description
This toolbox allows you to do simple mediation and moderation analysis.
Models are estimated with the 'lavaan' package by Rosseel (2012)
<doi:10.18637/jss.v048.i02>; standard errors for the mediation estimates
are computed with the delta method following Sobel (1982)
<doi:10.2307/270723> or by bootstrapping. It is also available as a module
for 'jamovi' (see <https://www.jamovi.org> for more information). You can
find an in depth tutorial on the 'lavaan' model syntax used for this
package on <https://lavaan.ugent.be/tutorial/index.html>.

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
