%global __brp_check_rpaths %{nil}
%global packname  FFdownload
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from Kenneth French's Website

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-plyr 

%description
Downloads all the datasets (you can exclude the daily ones or specify a
list of those you are targeting specifically) from Kenneth French's
Website at
<https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>,
process them and convert them to list of 'xts' (time series).

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
