%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCPA4
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data and Functions for "An R Companion to Political Analysis, Fourth Edition"

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-car 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lmtest 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-utils 

%description
Provides teaching-oriented functions and datasets for "An R Companion to
Political Analysis, Fourth Edition" (forthcoming 2026). Functions produce
readable tables and graphics for descriptive statistics, data
transformation, confidence intervals, hypothesis testing, comparisons,
cross-tabulation, and linear and logistic regression. Sampling weights are
supported where appropriate, and analysis functions return reusable
results for further examination. The package also includes curated
political datasets designed for classroom instruction and independent
practice. See Edwards and Pollock (forthcoming 2026)
<https://www.poliscidata.com/textbooks/r_companion_4e.php>.

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
