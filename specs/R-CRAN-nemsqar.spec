%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nemsqar
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          National Emergency Medical Service Quality Alliance Measure Calculations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Designed to automate the calculation of Emergency Medical Service (EMS)
quality metrics, 'nemsqar' implements measures defined by the National EMS
Quality Alliance (NEMSQA). By providing reliable, evidence-based quality
assessments, the package supports EMS agencies, healthcare providers, and
researchers in evaluating and improving patient outcomes.  Users can find
details on all approved NEMSQA measures at
<https://www.nemsqa.org/measures>.  Full technical specifications,
including documentation and pseudocode used to develop 'nemsqar', are
available on the NEMSQA website after creating a user profile at
<https://www.nemsqa.org>.

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
