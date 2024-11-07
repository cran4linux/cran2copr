%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psidR
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Build Panel Data Sets from PSID Raw Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-SAScii 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-futile.logger 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-SAScii 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-futile.logger 

%description
Makes it easy to build panel data in wide format from Panel Survey of
Income Dynamics (PSID) delivered raw data. Downloads data directly from
the PSID server using the 'SAScii' package. 'psidR' takes care of merging
data from each wave onto a cross-period index file, so that individuals
can be followed over time. The user must specify which years they are
interested in, and the 'PSID' variable names (e.g. ER21003) for each year
(they differ in each year). The package offers helper functions to
retrieve variable names from different waves. There are different panel
data designs and sample subsetting criteria implemented ("SRC", "SEO",
"immigrant" and "latino" samples). More information about the PSID can be
obtained at <https://simba.isr.umich.edu/data/data.aspx>.

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
