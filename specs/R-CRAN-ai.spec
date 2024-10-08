%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ai
%global packver   1.0.4.44
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4.44
Release:          1%{?dist}%{?buildtag}
Summary:          Build, Predict and Analyse Artificial Intelligence Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-Metrics 
Requires:         R-base 
Requires:         R-CRAN-class 
Requires:         R-stats 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-party 
Requires:         R-CRAN-Metrics 

%description
An interface for data processing, building models, predicting values and
analysing outcomes. Fitting Linear Models, Robust Fitting of Linear
Models, k-Nearest Neighbor Classification, 1-Nearest Neighbor
Classification, and Conditional Inference Trees are available.

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
