%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lme4breeding
%global packver   1.0.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.31
Release:          1%{?dist}%{?buildtag}
Summary:          Relationship-Based Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-Matrix >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-Matrix >= 1.0
Requires:         R-methods 
Requires:         R-CRAN-crayon 

%description
Fit relationship-based and customized mixed-effects models with complex
variance-covariance structures using the 'lme4' machinery. The core
computational algorithms are implemented using the 'Eigen' 'C++' library
for numerical linear algebra and 'RcppEigen' 'glue'.

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
