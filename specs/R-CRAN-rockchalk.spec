%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rockchalk
%global packver   1.8.157
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.157
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Estimation and Presentation

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-kutils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-carData 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-kutils 

%description
A collection of functions for interpretation and presentation of
regression analysis.  These functions are used to produce the statistics
lectures in <https://pj.freefaculty.org/guides/>. Includes regression
diagnostics, regression tables, and plots of interactions and "moderator"
variables. The emphasis is on "mean-centered" and "residual-centered"
predictors. The vignette 'rockchalk' offers a fairly comprehensive
overview.  The vignette 'Rstyle' has advice about coding in R.  The
package title 'rockchalk' refers to our school motto, 'Rock Chalk Jayhawk,
Go K.U.'.

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
