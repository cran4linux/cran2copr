%global packname  cglasso
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Graphical LASSO for Gaussian Graphical Models with Censored and Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-MASS 

%description
Conditional graphical lasso estimator is an extension of the graphical
lasso proposed to estimate the conditional dependence structure of a set
of p response variables given q predictors. This package provides suitable
extensions developed to study datasets with censored and/or missing
values. Standard conditional graphical lasso is available as a special
case. Furthermore, the package provides an integrated set of core routines
for visualization, analysis, and simulation of datasets with censored
and/or missing values drawn from a Gaussian graphical model. Details about
the implemented models can be found in Augugliaro et al. (2020b) <doi:
10.1007/s11222-020-09945-7>, Augugliaro et al. (2020a) <doi:
10.1093/biostatistics/kxy043>, Yin et al. (2001) <doi: 10.1214/11-AOAS494>
and Stadler et al. (2012) <doi: 10.1007/s11222-010-9219-7>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
