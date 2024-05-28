%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bmm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy and Accessible Bayesian Measurement Models Using 'brms'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms >= 2.21.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-brms >= 2.21.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-withr 

%description
Fit computational and measurement models using full Bayesian inference.
The package provides a simple and accessible interface by translating
complex domain-specific models into 'brms' syntax, a powerful and flexible
framework for fitting Bayesian regression models using 'Stan'. The package
is designed so that users can easily apply state-of-the-art models in
various research fields, and so that researchers can use it as a new model
development framework. References: Frischkorn and Popov (2023)
<doi:10.31234/osf.io/umt57>.

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
