%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  earthdatalogin
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          NASA 'EarthData' Access Utilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 

%description
Providing easy, portable access to NASA 'EarthData' products through the
use of bearer tokens. Much of NASA's public data catalogs hosted and
maintained by its 12 Distributed Active Archive Centers ('DAACs') are now
made available on the Amazon Web Services 'S3' storage.  However,
accessing this data through the standard 'S3' API is restricted to only to
compute resources running inside 'us-west-2' Data Center in Portland,
Oregon, which allows NASA to avoid being charged data egress rates. This
package provides public access to the data from any networked device by
using the 'EarthData' login application programming interface (API),
<https://www.earthdata.nasa.gov/data/earthdata-login>, providing
convenient authentication and access to cloud-hosted NASA 'EarthData'
products. This makes access to a wide range of earth observation data from
any location straight forward and compatible with R packages that are
widely used with cloud native earth observation data (such as 'terra',
'sf', etc.)

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
