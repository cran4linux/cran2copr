%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEPaLS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage for Extreme Partial Least-Squares (SEPaLS)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Regression context for the Partial Least Squares framework for Extreme
values. Estimations of the Shrinkage for Extreme Partial Least-Squares
(SEPaLS) estimators, an adaptation of the original Partial Least Squares
(PLS) method tailored to the extreme-value framework. The SEPaLS project
is a joint work by Stephane Girard, Hadrien Lorenzo and Julyan Arbel. R
code to replicate the results of the paper is available at
<https://github.com/hlorenzo/SEPaLS_simus>. Extremes within PLS was
already studied by one of the authors, see M Bousebeta, G Enjolras, S
Girard (2023) <doi:10.1016/j.jmva.2022.105101>.

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
