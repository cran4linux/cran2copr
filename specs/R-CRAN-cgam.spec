%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cgam
%global packver   1.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.31
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Generalized Additive Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coneproj >= 1.20
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-coneproj >= 1.20
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-svDialogs 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-CRAN-zeallot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-MASS 

%description
A constrained generalized additive model is fitted by the cgam routine.
Given a set of predictors, each of which may have a shape or order
restrictions, the maximum likelihood estimator for the constrained
generalized additive model is found using an iteratively re-weighted cone
projection algorithm. The ShapeSelect routine chooses a subset of
predictor variables and describes the component relationships with the
response. For each predictor, the user needs only specify a set of
possible shape or order restrictions. A model selection method chooses the
shapes and orderings of the relationships as well as the variables. The
cone information criterion (CIC) is used to select the best combination of
variables and shapes. A genetic algorithm may be used when the set of
possible models is large. In addition, the cgam routine implements a
two-dimensional isotonic regression using warped-plane splines without
additivity assumptions.  It can also fit a convex or concave regression
surface with triangle splines without additivity assumptions. See Liao X,
Meyer MC (2019)<doi:10.18637/jss.v089.i05> for more details.

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
