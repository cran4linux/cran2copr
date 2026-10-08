%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coldstart
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibrating Generated Items Before Pretesting with Predicted Priors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Predicts Rasch item difficulty from item features (text embeddings from
any model, template family, content metadata) by ridge regression (Hoerl
and Kennard, 1970, <doi:10.1080/00401706.1970.10488634>) with honest
out-of-sample uncertainty, uses the predictions as robust informative
priors to calibrate new items from small pretest samples, in the spirit of
using collateral information in calibration (Mislevy, Sheehan and
Wingersky, 1993, <doi:10.1111/j.1745-3984.1993.tb00422.x>), plans the
pretest sample size needed for a target precision, and diagnoses item
families whose predictions cannot be trusted.

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
