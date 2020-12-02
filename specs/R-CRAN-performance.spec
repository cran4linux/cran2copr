%global packname  performance
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment of Regression Models Performance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-bayestestR >= 0.7.5
BuildRequires:    R-CRAN-insight >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-bayestestR >= 0.7.5
Requires:         R-CRAN-insight >= 0.11.0
Requires:         R-stats 
Requires:         R-utils 

%description
Utilities for computing measures to assess model quality, which are not
directly provided by R's 'base' or 'stats' packages. These include e.g.
measures like r-squared, intraclass correlation coefficient (Nakagawa,
Johnson & Schielzeth (2017) <doi:10.1098/rsif.2017.0213>), root mean
squared error or functions to check models for overdispersion, singularity
or zero-inflation and more. Functions apply to a large variety of
regression models, including generalized linear models, mixed effects
models and Bayesian models.

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
