%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geobounds
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Map Data from 'geoBoundaries'

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-tools 
Requires:         R-utils 

%description
Tools to download data from 'geoBoundaries'
<https://www.geoboundaries.org/>. Several administration levels available.
See Runfola, D. et al. (2020) geoBoundaries: A global database of
political administrative boundaries. PLOS ONE 15(4): 1-9.
<doi:10.1371/journal.pone.0231866>.

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
