%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  report
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Reporting of Results and Statistical Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 1.0.1
BuildRequires:    R-CRAN-effectsize >= 1.0.0
BuildRequires:    R-CRAN-datawizard >= 1.0.0
BuildRequires:    R-CRAN-parameters >= 0.24.1
BuildRequires:    R-CRAN-bayestestR >= 0.15.0
BuildRequires:    R-CRAN-performance >= 0.13.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-insight >= 1.0.1
Requires:         R-CRAN-effectsize >= 1.0.0
Requires:         R-CRAN-datawizard >= 1.0.0
Requires:         R-CRAN-parameters >= 0.24.1
Requires:         R-CRAN-bayestestR >= 0.15.0
Requires:         R-CRAN-performance >= 0.13.0
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
The aim of the 'report' package is to bridge the gap between R’s output
and the formatted results contained in your manuscript. This package
converts statistical models and data frames into textual reports suited
for publication, ensuring standardization and quality in results
reporting.

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
