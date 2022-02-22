%global __brp_check_rpaths %{nil}
%global packname  sglg
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Semi-Parametric Generalized log-Gamma Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AdequacyModel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-TeachingSampling 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-AdequacyModel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-TeachingSampling 

%description
Set of tools to fit a linear multiple or semi-parametric regression models
with the possibility of non-informative random right-censoring. Under this
setup, the localization parameter of the response variable distribution is
modeled by using linear multiple regression or semi-parametric functions,
whose non-parametric components may be approximated by natural cubic
spline or P-splines. The supported distribution for the model error is a
generalized log-gamma distribution which includes the generalized extreme
value and standard normal distributions as important special cases. Also,
some numerical and graphical devices for diagnostic of the fitted models
are offered.

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
