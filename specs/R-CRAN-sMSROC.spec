%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sMSROC
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Assessment of Diagnostic and Prognostic Markers

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-plotROC 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-CRAN-thregI 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-plotROC 
Requires:         R-CRAN-icenReg 
Requires:         R-CRAN-thregI 

%description
Provides estimations of the Receiver Operating Characteristic (ROC) curve
and the Area Under the Curve (AUC) based on the two-stages mixed-subjects
ROC curve estimator (Diaz-Coto et al. (2020) <doi:10.1515/ijb-2019-0097>
and Diaz-Coto et al. (2020) <doi:10.1080/00949655.2020.1736071>).

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
