%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLMMcosinor
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit a Cosinor Model Using a Generalised Mixed Modelling Framework

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Allows users to fit a cosinor model using the 'glmmTMB' framework. This
extends on existing cosinor modelling packages, including 'cosinor' and
'circacompare', by including a wide range of available link functions and
the capability to fit mixed models. The cosinor model is described by
Cornelissen (2014) <doi:10.1186/1742-4682-11-16>.

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
