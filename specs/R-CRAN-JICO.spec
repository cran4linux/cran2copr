%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JICO
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Joint and Individual Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlist 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlist 

%description
An R package that implements the JICO algorithm [Wang, P., Wang, H., Li,
Q., Shen, D., & Liu, Y. (2024). <Journal of Computational and Graphical
Statistics, 33(3), 763-773>]. It aims at solving the multi-group
regression problem. The algorithm decomposes the responses from multiple
groups into shared and group-specific components, which are driven by
low-rank approximations of joint and individual structures from the
covariates respectively.

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
