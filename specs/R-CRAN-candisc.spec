%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  candisc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Generalized Canonical Discriminant and Canonical Correlation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-heplots >= 0.8.6
BuildRequires:    R-CRAN-car 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-heplots >= 0.8.6
Requires:         R-CRAN-car 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 

%description
Functions for computing and visualizing generalized canonical discriminant
analyses and canonical correlation analysis for a multivariate linear
model. Traditional canonical discriminant analysis is restricted to a
one-way 'MANOVA' design and is equivalent to canonical correlation
analysis between a set of quantitative response variables and a set of
dummy variables coded from the factor variable. The 'candisc' package
generalizes this to higher-way 'MANOVA' designs for all factors in a
multivariate linear model, computing canonical scores and vectors for each
term. The graphic functions provide low-rank (1D, 2D, 3D) visualizations
of terms in an 'mlm' via the 'plot.candisc' and 'heplot.candisc' methods.
Related plots are now provided for canonical correlation analysis when all
predictors are quantitative. Methods for linear discriminant analysis are
now included.

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
