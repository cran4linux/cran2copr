%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contactsurveys
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Contact Surveys for Use in Infectious Disease Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-zen4R >= 0.10.3
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-oai 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-yesno 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-zen4R >= 0.10.3
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-oai 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-yesno 

%description
Download, cache, and manage social contact survey data from the social
contact data community on Zenodo
(<https://zenodo.org/communities/social_contact_data>) for use in
infectious disease modelling. Provides functions to list available
surveys, download survey files with automatic caching, and retrieve
citations. Contact survey data describe who contacts whom in a population
and are used to parameterise age-structured transmission models, for
example via the 'socialmixr' package. The surveys available include those
from the POLYMOD study (Mossong et al. (2008)
<doi:10.1371/journal.pmed.0050074>) and other social contact data shared
on Zenodo.

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
