%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enmpa
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Niche Modeling using Presence-Absence Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-snow 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
A set of tools to perform Ecological Niche Modeling with presence-absence
data. It includes algorithms for data partitioning, model fitting,
calibration, evaluation, selection, and prediction. Other functions help
to explore signals of ecological niche using univariate and multivariate
analyses, and model features such as variable response curves and variable
importance. Unique characteristics of this package are the ability to
exclude models with concave quadratic responses, and the option to clamp
model predictions to specific variables. These tools are implemented
following principles proposed in Cobos et al., (2022)
<doi:10.17161/bi.v17i.15985>, Cobos et al., (2019)
<doi:10.7717/peerj.6281>, and Peterson et al., (2008)
<doi:10.1016/j.ecolmodel.2007.11.008>.

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
