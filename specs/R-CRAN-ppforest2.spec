%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppforest2
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Pursuit Oblique Decision Trees and Random Forests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.11

%description
Builds decision trees by splitting on linear combinations of randomly
chosen variables. Projection pursuit is used to choose a projection of the
variables that best separates the groups. Using linear combinations of
variables to separate groups takes the correlation between variables into
account, which allows the model to outperform a traditional decision tree
when the separation between groups occurs in combinations of variables.
Single trees can be assembled into random forests for improved accuracy.
Implements projection pursuit classification trees (Lee, Cook, Park and
Lee (2013) <doi:10.1214/13-EJS810>) and projection pursuit forests (da
Silva, Cook and Lee (2021) <doi:10.1080/10618600.2020.1870480>), following
the earlier 'PPforest' package.

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
