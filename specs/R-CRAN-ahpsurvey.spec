%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ahpsurvey
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analytic Hierarchy Process for Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
The Analytic Hierarchy Process is a versatile multi-criteria
decision-making tool introduced by Saaty (1987)
<doi:10.1016/0270-0255(87)90473-8> that allows decision-makers to weigh
attributes and evaluate alternatives presented to them.  This package
provides a consistent methodology for researchers to reformat data and run
analytic hierarchy process in R on data that are formatted using the
survey data entry mode. It is optimized for performing the analytic
hierarchy process with many decision-makers, and provides tools and
options for researchers to aggregate individual preferences and test
multiple options. It also allows researchers to quantify, visualize and
correct for inconsistency in the decision-maker's comparisons.

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
