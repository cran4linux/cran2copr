%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EQUALPrognosis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysing Prognostic Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-CalibrationCurves 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-predtools 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-CalibrationCurves 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-predtools 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-stringr 

%description
Functions that help with analysis of prognostic study data. This allows
users with little experience of developing models to develop models and
assess the performance of the prognostic models. This also summarises the
information, so the performance of multiple models can be displayed
simultaneously. Gurusamy, K
(2026)<https://github.com/kurinchi2k/EQUALPrognosis>.

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
