%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  micemd
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Imputation by Chained Equations with Multilevel Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jomo >= 2.6.3
BuildRequires:    R-CRAN-mice >= 2.42
BuildRequires:    R-CRAN-mvmeta >= 0.4.7
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-GJRM 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mixmeta 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-jomo >= 2.6.3
Requires:         R-CRAN-mice >= 2.42
Requires:         R-CRAN-mvmeta >= 0.4.7
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-GJRM 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mixmeta 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-ggplot2 

%description
Addons for the 'mice' package to perform multiple imputation using chained
equations with two-level data. Includes imputation methods dedicated to
sporadically and systematically missing values. Imputation of continuous,
binary or count variables are available. Following the recommendations of
Audigier, V. et al (2018) <doi:10.1214/18-STS646>, the choice of the
imputation method for each variable can be facilitated by a default choice
tuned according to the structure of the incomplete dataset. Allows
parallel calculation and overimputation for 'mice'.

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
