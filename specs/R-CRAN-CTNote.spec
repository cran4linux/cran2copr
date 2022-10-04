%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CTNote
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          CTN Outcomes, Treatments, and Endpoints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 

%description
The Clinical Trials Network (CTN) of the U.S. National Institute of Drug
Abuse sponsored the CTN-0094 research team to harmonize data sets from
three nationally-representative clinical trials for opioid use disorder
(OUD). The CTN-0094 team herein provides a coded collection of trial
outcomes and endpoints used in various OUD clinical trials over the past
50 years. These coded outcome functions are used to contrast and cluster
different clinical outcome functions based on daily or weekly patient
urine screenings. Note that we abbreviate urine drug screen as "UDS" and
urine opioid screen as "UOS". For the example data sets (based on clinical
trials data harmonized by the CTN-0094 research team), UDS and UOS are
largely interchangeable.

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
