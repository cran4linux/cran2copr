%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landmulti
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Landmark Prediction with Multiple Short-Term Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-landpred 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-snow 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-landpred 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-snow 

%description
Contains functions for a flexible varying-coefficient landmark model by
incorporating multiple short-term events into the prediction of long-term
survival probability. For more information about landmark prediction
please see Li, W., Ning, J., Zhang, J., Li, Z., Savitz, S.I., Tahanan, A.,
Rahbar.M.H., (2023+). "Enhancing Long-term Survival Prediction with
Multiple Short-term Events: Landmarking with A Flexible Varying
Coefficient Model".

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
