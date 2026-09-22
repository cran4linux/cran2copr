%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tiltdens
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tilted and Data-Sharpened Nonparametric Density Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
High-order nonparametric density estimators built by perturbing a
conventional kernel estimator, either by re-weighting the observations
("tilting") or by moving them ("data sharpening"). The perturbation is
chosen so that the estimator inherits the fast convergence rate of an
infinite-order kernel estimator, such as the sinc or trapezoidal flat-top
estimator, while remaining a proper non-negative density without the
oscillatory tails those estimators suffer from. Two criteria are provided:
minimising the L2 distance to an infinite-order comparator, following
Doosti and Hall (2016) <doi:10.1111/rssb.12112>, and minimising a
cross-validation criterion that needs no comparator and is much faster,
following Doosti, Hall and Mateu (2018) <doi:10.1016/j.jspi.2017.12.003>.

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
