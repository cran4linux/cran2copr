%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  validate
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Validation Infrastructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-CRAN-yaml 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-settings 
Requires:         R-CRAN-yaml 

%description
Declare data validation rules and data quality indicators; confront data
with them and analyze or visualize the results. The package supports rules
that are per-field, in-record, cross-record or cross-dataset. Rules can be
automatically analyzed for rule type and connectivity. Supports checks
implied by an SDMX DSD file as well. See also Van der Loo and De Jonge
(2018) <doi:10.1002/9781118897126>, Chapter 6 and the JSS paper (2021)
<doi:10.18637/jss.v097.i10>.

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
