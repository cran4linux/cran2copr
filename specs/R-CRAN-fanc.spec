%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fanc
%global packver   2.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Likelihood Factor Analysis via Nonconvex Penalty

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ellipse 
Requires:         R-tcltk 

%description
Computes the penalized maximum likelihood estimates of factor loadings and
unique variances for various tuning parameters. The pathwise coordinate
descent along with EM algorithm is used.  This package also includes a new
graphical tool which outputs path diagram, goodness-of-fit indices and
model selection criteria for each regularization parameter. The user can
change the regularization parameter by manipulating scrollbars, which is
helpful to find a suitable value of regularization parameter.

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
