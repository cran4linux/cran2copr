%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  googleCloudRunner
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Scripts in the Google Cloud via Cloud Run, Cloud Build and Cloud Scheduler

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-yaml >= 2.2.0
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-googleAuthR >= 2.0.0
BuildRequires:    R-CRAN-usethis >= 1.6.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-openssl >= 1.4.1
BuildRequires:    R-CRAN-plumber >= 1.0.0
BuildRequires:    R-CRAN-jose >= 1.0
BuildRequires:    R-CRAN-googleCloudStorageR >= 0.7.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-googlePubsubR >= 0.0.2
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-yaml >= 2.2.0
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-googleAuthR >= 2.0.0
Requires:         R-CRAN-usethis >= 1.6.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-openssl >= 1.4.1
Requires:         R-CRAN-plumber >= 1.0.0
Requires:         R-CRAN-jose >= 1.0
Requires:         R-CRAN-googleCloudStorageR >= 0.7.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-googlePubsubR >= 0.0.2
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Tools to easily enable R scripts in the Google Cloud Platform. Utilise
cloud services such as Cloud Run <https://cloud.google.com/run/> for R
over HTTP, Cloud Build <https://cloud.google.com/build> for Continuous
Delivery and Integration services and Cloud Scheduler
<https://cloud.google.com/scheduler/> for scheduled scripts.

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
