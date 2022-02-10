%global __brp_check_rpaths %{nil}
%global packname  mlmi
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Multiple Imputation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-cat 
BuildRequires:    R-CRAN-mix 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-cat 
Requires:         R-CRAN-mix 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nlme 

%description
Implements so called Maximum Likelihood Multiple Imputation as described
by von Hippel and Bartlett (2021) <doi:10.1214/20-STS793>. A number of
different imputations are available, by utilising the 'norm', 'cat' and
'mix' packages. Inferences can be performed either using combination rules
similar to Rubin's or using a likelihood score based approach based on
theory by Wang and Robins (1998) <doi:10.1093/biomet/85.4.935>.

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
