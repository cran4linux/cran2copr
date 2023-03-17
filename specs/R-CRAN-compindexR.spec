%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compindexR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Composite Index

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.1.0
BuildRequires:    R-CRAN-pracma >= 2.3.8
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-NlcOptim >= 0.6
Requires:         R-CRAN-car >= 3.1.0
Requires:         R-CRAN-pracma >= 2.3.8
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-NlcOptim >= 0.6

%description
It uses the first-order sensitivity index to measure whether the weights
assigned by the creator of the composite indicator match the actual
importance of the variables. Moreover, the variance inflation factor is
used to reduce the set of correlated variables. In the case of a
discrepancy between the importance and the assigned weight, the script
determines weights that allow adjustment of the weights to the intended
impact of variables. If the optimised weights are unable to reflect the
desired importance, the highly correlated variables are reduced, taking
into account variance inflation factor. The final outcome of the script is
the calculated value of the composite indicator based on optimal weights
and a reduced set of variables, and the linear ordering of the analysed
objects.

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
