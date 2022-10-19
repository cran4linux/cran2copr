%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidytags
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Importing and Analyzing 'Twitter' Data Collected with 'Twitter Archiving Google Sheets'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-googlesheets4 >= 1.0
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-rtweet >= 1.0
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-googlesheets4 >= 1.0
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-rtweet >= 1.0

%description
The 'tidytags' package coordinates the simplicity of collecting tweets
over time with a 'Twitter Archiving Google Sheet' (TAGS;
<https://tags.hawksey.info/>) and the utility of the 'rtweet' package
(<https://docs.ropensci.org/rtweet/>) for processing and preparing
additional 'Twitter' metadata. 'tidytags' also introduces functions
developed to facilitate systematic yet flexible analyses of data from
'Twitter'.

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
