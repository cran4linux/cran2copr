%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSIM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Preference Selection Index Method (PSIM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyverse 

%description
The Preference Selection Index Method was created in (2010) and provides
an innovative approach to determining the relative importance of criteria
without pairwise comparisons, unlike the Analytic Hierarchy Process. The
Preference Selection Index Method uses statistical methods to calculate
the criteria weights and reflects their relative importance in the final
decision-making process, offering an objective and non-subjective
solution. This method is beneficial in multi-criteria decision analysis.
The 'PSIM' package provides a practical and accessible tool for
implementing the Preference Selection Index Method in R. It calculates the
weights of criteria and makes the method available to researchers,
analysts, and professionals without the need to develop complex
calculations manually. More details about the Preference Selection Index
Method can be found in Maniya K. and Bhatt M. G.(2010)
<doi:10.1016/j.matdes.2009.11.020>.

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
