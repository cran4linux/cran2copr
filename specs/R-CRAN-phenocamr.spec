%global __brp_check_rpaths %{nil}
%global packname  phenocamr
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Facilitates 'PhenoCam' Data Access and Time Series Post-Processing

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-daymetr 
BuildRequires:    R-CRAN-MODISTools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-zoo 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-daymetr 
Requires:         R-CRAN-MODISTools 

%description
Programmatic interface to the 'PhenoCam' web services
(<https://phenocam.nau.edu/webcam>). Allows for easy downloading of
'PhenoCam' data directly to your R workspace or your computer and provides
post-processing routines for consistent and easy timeseries outlier
detection, smoothing and estimation of phenological transition dates.
Methods for this package are described in detail in Hufkens et. al (2018)
<doi:10.1111/2041-210X.12970>.

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
