%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optweight
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimization-Based Stable Balancing Weights

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cli >= 3.6.5
BuildRequires:    R-CRAN-collapse >= 2.1.5
BuildRequires:    R-CRAN-Matrix >= 1.2.13
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-osqp >= 0.6.3.3
BuildRequires:    R-CRAN-chk >= 0.10.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cli >= 3.6.5
Requires:         R-CRAN-collapse >= 2.1.5
Requires:         R-CRAN-Matrix >= 1.2.13
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-osqp >= 0.6.3.3
Requires:         R-CRAN-chk >= 0.10.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Use optimization to estimate weights that balance covariates for binary,
multi-category, continuous, and multivariate treatments in the spirit of
Zubizarreta (2015) <doi:10.1080/01621459.2015.1023805>. The degree of
balance can be specified for each covariate. In addition, sampling weights
can be estimated that allow a sample to generalize to a population
specified with given target moments of covariates, as in matching-adjusted
indirect comparison (MAIC).

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
