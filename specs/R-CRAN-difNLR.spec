%global packname  difNLR
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          DIF and DDF Detection by Non-Linear Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-calculus 
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-calculus 
Requires:         R-CRAN-CTT 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Detection of differential item functioning (DIF) among dichotomously
scored items and differential distractor functioning (DDF) among unscored
items with non-linear regression procedures based on generalized logistic
regression models (Drabinova & Martinkova, 2017,
<doi:10.1111/jedm.12158>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
