%global __brp_check_rpaths %{nil}
%global packname  cgmquantify
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Glucose and Glucose Variability

License:          MIT License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hms 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
Continuous glucose monitoring (CGM) systems provide real-time, dynamic
glucose information by tracking interstitial glucose values throughout the
day. Glycemic variability, also known as glucose variability, is an
established risk factor for hypoglycemia (Kovatchev) and has been shown to
be a risk factor in diabetes complications. Over 20 metrics of glycemic
variability have been identified. Here, we provide functions to calculate
glucose summary metrics, glucose variability metrics (as defined in
clinical publications), and visualizations to visualize trends in CGM
data. Cho P, Bent B, Wittmann A, et al. (2020)
<https://diabetes.diabetesjournals.org/content/69/Supplement_1/73-LB.abstract>
American Diabetes Association (2020)
<https://professional.diabetes.org/diapro/glucose_calc> Kovatchev B (2019)
<doi:10.1177/1932296819826111> Kovdeatchev BP (2017)
<doi:10.1038/nrendo.2017.3> Tamborlane W V., Beck RW, Bode BW, et al.
(2008) <doi:10.1056/NEJMoa0805017> Umpierrez GE, P. Kovatchev B (2018)
<doi:10.1016/j.amjms.2018.09.010>.

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
