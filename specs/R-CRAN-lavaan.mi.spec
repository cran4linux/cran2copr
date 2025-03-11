%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavaan.mi
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Structural Equation Models to Multiply Imputed Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.18
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lavaan >= 0.6.18
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The primary purpose of 'lavaan.mi' is to extend the functionality of the R
package 'lavaan', which implements structural equation modeling (SEM).
When incomplete data have been multiply imputed, the imputed data sets can
be analyzed by 'lavaan' using complete-data estimation methods, but
results must be pooled across imputations (Rubin, 1987,
<doi:10.1002/9780470316696>). The 'lavaan.mi' package automates the
pooling of point and standard-error estimates, as well as a variety of
test statistics, using a familiar interface that allows users to fit an
SEM to multiple imputations as they would to a single data set using the
'lavaan' package.

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
