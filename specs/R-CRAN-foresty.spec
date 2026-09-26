%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  foresty
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Plots and Subgroup Effects from Fitted Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-car >= 3.1.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-patchwork >= 1.1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-car >= 3.1.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-patchwork >= 1.1.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Draws forest plots of exposure effects from fitted regression models. Name
an exposure and 'foresty' plots its effect. Name an effect modifier as
well and it refits the model with the interaction term, estimates the
exposure effect within each level of the modifier as a linear combination
of the coefficients, and reports the joint interaction test beside those
estimates. It takes one exposure and one modifier at a time, so the
interaction is always a two-way one. Rows of the plot and of the table
beside it share one scale, in a layout that can follow a journal's house
style. The same results go to a self-contained HTML page holding the
subgroup estimates, the joint test and the coefficient table. The 'car'
package computes the linear combinations and their tests. Models fitted by
stats::glm(), stats::lm(), the 'survival' package, the 'lme4' package, the
'geepack' package and the 'survey' package are supported, as is any fit
supplying coef() and vcov(). Ordinal outcomes are supported through the
'MASS' package and nominal ones through the 'nnet' package, where the
figure carries one row per level of the outcome and the interaction is
tested jointly across the equations. Fits from the 'rms' package are
refused, naming the function that fits the same model in their place. The
estimation of an exposure effect within a level of a modifier, and the
test of the difference between such estimates, follow Altman and Bland
(2003) <doi:10.1136/bmj.326.7382.219> and VanderWeele and Knol (2014)
<doi:10.1515/em-2013-0005>; the reporting of subgroup effects beside the
interaction test follows Wang et al. (2007) <doi:10.1056/NEJMsr077003>,
and the figure itself the forest plot described by Lewis and Clarke (2001)
<doi:10.1136/bmj.322.7300.1479>.

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
