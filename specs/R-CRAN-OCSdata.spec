%global __brp_check_rpaths %{nil}
%global packname  OCSdata
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Download Data from the 'Open Case Studies' Repository

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 2.0.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-usethis >= 2.0.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-purrr >= 0.3.0

%description
Provides functions to access and download data from the 'Open Case
Studies' <https://www.opencasestudies.org/> repositories on 'GitHub'
<https://github.com/opencasestudies>. Different functions enable users to
grab the data they need at different sections in the case study, as well
as download the whole case study repository. All the user needs to do is
input the name of the case study being worked on. The package relies on
the httr::GET() function to access files through the 'GitHub' API. The
functions usethis::use_zip() and usethis::create_from_github() are used to
clone and/or download the case study repositories. To cite an individual
case study, please see the respective 'README' file at
<https://github.com/opencasestudies/>.
<https://github.com/opencasestudies/ocs-bp-rural-and-urban-obesity>
<https://github.com/opencasestudies/ocs-bp-air-pollution>
<https://github.com/opencasestudies/ocs-bp-vaping-case-study>
<https://github.com/opencasestudies/ocs-bp-opioid-rural-urban>
<https://github.com/opencasestudies/ocs-bp-RTC-wrangling>
<https://github.com/opencasestudies/ocs-bp-RTC-analysis>
<https://github.com/opencasestudies/ocs-bp-youth-disconnection>
<https://github.com/opencasestudies/ocs-bp-youth-mental-health>
<https://github.com/opencasestudies/ocs-bp-school-shootings-dashboard>
<https://github.com/opencasestudies/ocs-bp-co2-emissions>
<https://github.com/opencasestudies/ocs-bp-diet>.

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
