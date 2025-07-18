%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rquefts
%global packver   1.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Evaluation of the Native Fertility of Tropical Soils

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-meteor 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-meteor 
Requires:         R-methods 

%description
An implementation of the QUEFTS (Quantitative Evaluation of the Native
Fertility of Tropical Soils) model. The model (1) estimates native
nutrient (N, P, K) supply of soils from a few soil chemical properties;
and (2) computes crop yield given that supply, crop parameters, fertilizer
application, and crop attainable yield. See Janssen et al. (1990)
<doi:10.1016/0016-7061(90)90021-Z> for the technical details and Sattari
et al. (2014) <doi:10.1016/j.fcr.2013.12.005> for a recent evaluation and
improvements.

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
