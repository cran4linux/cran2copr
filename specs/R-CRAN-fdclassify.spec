%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdclassify
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Supervised Classification for Functional Data via Signed Depth

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-modeest 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-modeest 

%description
Provides a suite of supervised classifiers for functional data based on
the concept of signed depth. The core pipeline computes Fraiman-Muniz (FM)
functional depth in either its Tukey or Simplicial variant, derives a
signed depth by comparing each curve to a reference median curve via the
signed distance integral, and feeds the resulting scalar summary into
several classifiers: the k-Ranked Nearest Neighbour (k-RNN) rule, a
moving-average smoother, a kernel-density Bayes rule, logistic regression
on signed depth and distance to the mode, and a generalised additive model
(GAM) classifier. Cross-validation routines for tuning the neighbourhood
size k and parametric bootstrap confidence intervals are also included.

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
