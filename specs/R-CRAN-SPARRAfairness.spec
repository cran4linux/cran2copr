%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPARRAfairness
%global packver   0.1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Differential Behaviour of SPARRA Score Across Demographic Groups

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cvAUC 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cvAUC 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 

%description
The SPARRA risk score (Scottish Patients At Risk of admission and
Re-Admission) estimates yearly risk of emergency hospital admission using
electronic health records on a monthly basis for most of the Scottish
population. This package implements a suite of functions used to analyse
the behaviour and performance of the score, focusing particularly on
differential performance over demographically-defined groups. It includes
useful utility functions to plot receiver-operator-characteristic,
precision-recall and calibration curves, draw stock human figures,
estimate counterfactual quantities without the need to re-compute risk
scores, to simulate a semi-realistic dataset. Our manuscript can be found
at: <doi:10.1371/journal.pdig.0000675>.

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
