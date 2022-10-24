%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gld
%global packver   2.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Use of the Generalised (Tukey) Lambda Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-lmom 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-lmom 

%description
The generalised lambda distribution, or Tukey lambda distribution,
provides a wide variety of shapes with one functional form. This package
provides random numbers, quantiles, probabilities, densities and density
quantiles for four different types of the distribution, the FKML (Freimer
et al 1988), RS (Ramberg and Schmeiser 1974), GPD (van Staden and Loots
2009) and FM5 - see documentation for details. It provides the density
function, distribution function, and Quantile-Quantile plots. It
implements a variety of estimation methods for the distribution, including
diagnostic plots. Estimation methods include the starship (all 4 types),
method of L-Moments for the GPD and FKML types, and a number of methods
for only the FKML type. These include maximum likelihood, maximum product
of spacings, Titterington's method, Moments, Trimmed L-Moments and
Distributional Least Absolutes.

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
