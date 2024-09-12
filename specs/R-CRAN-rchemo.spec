%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rchemo
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dimension Reduction, Regression and Discrimination for Chemometrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-e1071 
Requires:         R-utils 

%description
Data exploration and prediction with focus on high dimensional data and
chemometrics. The package was initially designed about partial least
squares regression and discrimination models and variants, in particular
locally weighted PLS models (LWPLS). Then, it has been expanded to many
other methods for analyzing high dimensional data. The name 'rchemo' comes
from the fact that the package is orientated to chemometrics, but most of
the provided methods are fully generic to other domains. Functions such as
transform(), predict(), coef() and summary() are available. Tuning the
predictive models is facilitated by generic functions gridscore()
(validation dataset) and gridcv() (cross-validation). Faster versions are
also available for models based on latent variables (LVs) (gridscorelv()
and gridcvlv()) and ridge regularization (gridscorelb() and gridcvlb()).

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
