%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brokenstick
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Broken Stick Model for Irregular Longitudinal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-matrixsampling 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-matrixsampling 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Data on multiple individuals through time are often sampled at times that
differ between persons. Irregular observation times can severely
complicate the statistical analysis of the data. The broken stick model
approximates each subject’s trajectory by one or more connected line
segments. The times at which segments connect (breakpoints) are identical
for all subjects and under control of the user. A well-fitting broken
stick model effectively transforms individual measurements made at
irregular times into regular trajectories with common observation times.
Specification of the model requires just three variables: time,
measurement and subject. The model is a special case of the linear mixed
model, with time as a linear B-spline and subject as the grouping factor.
The main assumptions are: subjects are exchangeable, trajectories between
consecutive breakpoints are straight, random effects follow a multivariate
normal distribution, and unobserved data are missing at random. The
package contains functions for fitting the broken stick model to data, for
predicting curves in new data and for plotting broken stick estimates. The
package supports two optimization methods, and includes options to
structure the variance-covariance matrix of the random effects. The
analyst may use the software to smooth growth curves by a series of
connected straight lines, to align irregularly observed curves to a common
time grid, to create synthetic curves at a user-specified set of
breakpoints, to estimate the time-to-time correlation matrix and to
predict future observations. For additional documentation on background,
methodology and applications see
<https://growthcharts.org/brokenstick/articles/manual/manual.html>.

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
