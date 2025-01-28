%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oncmap
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Data from Electronic Adherence Monitoring Devices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.60
Requires:         R-core >= 3.60
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-readr 
Requires:         R-methods 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-zoo 

%description
Medication adherence, defined as medication-taking behavior that aligns
with the agreed-upon treatment protocol, is critical for realizing the
benefits of prescription medications. Medication adherence can be assessed
using electronic adherence monitoring devices (EAMDs), pill bottles or
boxes that contain a computer chip that records the date and time of each
opening (or “actuation”). Before researchers can use EAMD data, they must
apply a series of decision rules to transform actuation data into
adherence data. The purpose of this R package ('oncmap') is to transform
EAMD actuations in the form of a raw .csv file, information about the
patient, regimen, and non-monitored periods into two daily adherence
values -- Dose Taken and Correct Dose Taken.

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
