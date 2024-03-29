%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmvtnorm
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Truncated Multivariate Normal and Student t Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-gmm 
Requires:         R-stats 
Requires:         R-methods 

%description
Random number generation for the truncated multivariate normal and Student
t distribution. Computes probabilities, quantiles and densities, including
one-dimensional and bivariate marginal densities. Computes first and
second moments (i.e. mean and covariance matrix) for the double-truncated
multinormal case.

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
