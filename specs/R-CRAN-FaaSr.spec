%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FaaSr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'FaaSr' Local Test Development Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-uuid 

%description
Provides a local execution environment for testing and developing the
'FaaSr' workflows without requiring cloud infrastructure. The 'FaaSr'
package enables R developers to validate and test workflows locally before
deploying to Function-as-a-Service (FaaS) platforms. Key features include:
1) Parsing and validating JSON workflow configurations compliant with the
'FaaSr' schema 2) Simulated S3 storage operations using local file system
with local logging 3) Support for conditional branching 4) Support for
parallel rank functions execution 5) Workflow cycle detection and
validation 6) No cloud credentials or infrastructure required for testing
This package is designed for development and testing purposes. For
production deployment to cloud FaaS platforms, use the main 'FaaSr'
package available at <https://faasr.io/>.

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
