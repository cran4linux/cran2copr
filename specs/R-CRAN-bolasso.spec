%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bolasso
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Consistent Lasso Estimation Through the Bootstrap

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 3.0
BuildRequires:    R-CRAN-future.apply >= 1.1.0
BuildRequires:    R-CRAN-Matrix >= 1.0.6
BuildRequires:    R-CRAN-gamlr >= 1.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-glmnet >= 3.0
Requires:         R-CRAN-future.apply >= 1.1.0
Requires:         R-CRAN-Matrix >= 1.0.6
Requires:         R-CRAN-gamlr >= 1.0
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Implements the bolasso algorithm for consistent variable selection and
estimation accuracy. Includes support for many parallel backends via the
future package. For details see: Bach (2008), 'Bolasso: model consistent
Lasso estimation through the bootstrap', <doi:10.48550/arXiv.0804.1302>.

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
