%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tern.gee
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tables and Graphs for Generalized Estimating Equations (GEE) Model Fits

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans >= 1.4.5
BuildRequires:    R-CRAN-tern >= 0.9.3
BuildRequires:    R-CRAN-rtables >= 0.6.6
BuildRequires:    R-CRAN-formatters >= 0.5.5
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-geeasy 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
Requires:         R-CRAN-emmeans >= 1.4.5
Requires:         R-CRAN-tern >= 0.9.3
Requires:         R-CRAN-rtables >= 0.6.6
Requires:         R-CRAN-formatters >= 0.5.5
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-geeasy 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-nlme 
Requires:         R-stats 

%description
Generalized estimating equations (GEE) are a popular choice for analyzing
longitudinal binary outcomes. This package provides an interface for
fitting GEE, currently for logistic regression, within the 'tern'
<https://cran.r-project.org/package=tern> framework (Zhu, Sabanés Bové et
al., 2023) and tabulate results easily using 'rtables'
<https://cran.r-project.org/package=rtables> (Becker, Waddell et al.,
2023). It builds on 'geepack' <doi:10.18637/jss.v015.i02> (Højsgaard,
Halekoh and Yan, 2006) for the actual GEE model fitting.

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
