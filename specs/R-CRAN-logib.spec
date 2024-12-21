%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logib
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Salary Analysis by the Swiss Federal Office for Gender Equality

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of the Swiss Confederation's standard analysis model for
salary analyses
<https://www.ebg.admin.ch/en/equal-pay-analysis-with-logib> in R. The
analysis is run at company-level and the model is intended for
medium-sized and large companies. It can technically be used with 50 or
more employees (apprentices, trainees/interns and expats are not included
in the analysis). Employees with at least 100 employees are required by
the Gender Equality Act to conduct an equal pay analysis. This package
allows users to run the equal salary analysis in R, providing additional
transparency with respect to the methodology and simple automation
possibilities.

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
