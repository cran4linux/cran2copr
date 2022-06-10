%global __brp_check_rpaths %{nil}
%global packname  rankrate
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Preference Learning with Rankings and Ratings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-stats 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-lpSolve 

%description
An implementation of the statistical methodology proposed by Pearce and
Erosheva, "A Unified Statistical Learning Model for Rankings and Scores
with Application to Grant Panel Review" (2022), which at time of release
has been accepted in the Journal of Machine Learning Research. The package
provides tools for estimating parameters of a Mallows-Binomial model, the
first joint statistical preference learning model for rankings and
ratings. The package includes functions for simulating rankings and
ratings from the model, calculating the density of Mallows-Binomial data,
estimating parameters using various exact and approximate algorithms, and
for obtaining approximate confidence intervals based on the nonparametric
bootstrap.

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
