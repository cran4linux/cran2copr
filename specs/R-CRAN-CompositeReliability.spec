%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompositeReliability
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Determine the Composite Reliability of a Naturalistic, Unbalanced Dataset

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidyr 

%description
The reliability of assessment tools is a crucial aspect of monitoring
student performance in various educational settings. It ensures that the
assessment outcomes accurately reflect a student's true level of
performance. However, when assessments are combined, determining composite
reliability can be challenging, especially for naturalistic and unbalanced
datasets. This package provides an easy-to-use solution for calculating
composite reliability for different assessment types. It allows for the
inclusion of weight per assessment type and produces extensive G- and
D-study results with graphical interpretations. Overall, our approach
enhances the reliability of composite assessments, making it suitable for
various education contexts.

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
