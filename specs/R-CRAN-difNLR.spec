%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  difNLR
%global packver   1.4.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          DIF and DDF Detection by Non-Linear Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-calculus 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-calculus 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Detection of differential item functioning (DIF) among dichotomously
scored items and differential distractor functioning (DDF) among unscored
items with non-linear regression procedures based on generalized logistic
regression models (Hladka & Martinkova, 2020, <doi:10.32614/RJ-2020-014>).

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
