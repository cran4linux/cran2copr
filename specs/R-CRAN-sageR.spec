%global __brp_check_rpaths %{nil}
%global packname  sageR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Applied Statistics for Economics and Management with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
Datasets and functions for the book "Statistiques pour l’économie et la
gestion", "Théorie et applications en entreprise", F. Bertrand, Ch.
Derquenne, G. Dufrénot, F. Jawadi and M. Maumy, C. Borsenberger editor,
(2021, ISBN:9782807319448, De Boeck Supérieur, Louvain-la-Neuve). The
first chapter of the book is dedicated to an introduction to statistics
and their world. The second chapter deals with univariate exploratory
statistics and graphics. The third chapter deals with bivariate and
multivariate exploratory statistics and graphics. The fourth chapter is
dedicated to data exploration with Principal Component Analysis. The fifth
chapter is dedicated to data exploration with Correspondance Analysis. The
sixth chapter is dedicated to data exploration with Multiple
Correspondance Analysis. The seventh chapter is dedicated to data
exploration with automatic clustering. The eighth chapter is dedicated to
an introduction to probability theory and classical probability
distributions. The ninth chapter is dedicated to an estimation theory,
one-sample and two-sample tests. The tenth chapter is dedicated to an
Gaussian linear model. The eleventh chapter is dedicated to an
introduction to time series. The twelfth chapter is dedicated to an
introduction to probit and logit models. Various example datasets are
shipped with the package as well as some new functions.

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
