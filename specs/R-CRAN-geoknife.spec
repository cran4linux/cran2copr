%global __brp_check_rpaths %{nil}
%global packname  geoknife
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Web-Processing of Large Gridded Datasets

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-xml2 
Requires:         R-methods 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-sp 
Requires:         R-utils 

%description
Processes gridded datasets found on the U.S. Geological Survey Geo Data
Portal web application or elsewhere, using a web-enabled workflow that
eliminates the need to download and store large datasets that are reliably
hosted on the Internet. The package provides access to several data subset
and summarization algorithms that are available on remote web processing
servers (Read et al. (2015) <doi:10.1111/ecog.01880>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
