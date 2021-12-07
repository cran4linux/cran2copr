%global __brp_check_rpaths %{nil}
%global packname  cfda
%global packver   0.9.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.10
Release:          1%{?dist}%{?buildtag}
Summary:          Categorical Functional Data Analysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-mgcv 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 

%description
Package for the analysis of categorical functional data. The main purpose
is to compute an encoding (real functional variable) for each state
<doi:10.1080/00031305.2017.1375990>. It also provides functions to perform
basic statistical analysis on categorical functional data.

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
