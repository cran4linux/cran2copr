%global __brp_check_rpaths %{nil}
%global packname  cgam
%global packver   1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Generalized Additive Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-splines >= 3.4.0
BuildRequires:    R-Matrix >= 1.2.8
BuildRequires:    R-CRAN-coneproj >= 1.12
BuildRequires:    R-CRAN-lme4 >= 1.1.13
BuildRequires:    R-CRAN-svDialogs >= 0.9.57
Requires:         R-splines >= 3.4.0
Requires:         R-Matrix >= 1.2.8
Requires:         R-CRAN-coneproj >= 1.12
Requires:         R-CRAN-lme4 >= 1.1.13
Requires:         R-CRAN-svDialogs >= 0.9.57

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
Meyer MC (2019)<doi: 10.18637/jss.v089.i05> for more details.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
