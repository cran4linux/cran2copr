%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GGIR
%global packver   3.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Raw Accelerometer Data Analysis

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-unisensR 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-GGIRread 
BuildRequires:    R-CRAN-ActCR 
BuildRequires:    R-CRAN-read.gt3x 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-unisensR 
Requires:         R-CRAN-ineq 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-GGIRread 
Requires:         R-CRAN-ActCR 
Requires:         R-CRAN-read.gt3x 

%description
A tool to process and analyse data collected with wearable raw
acceleration sensors as described in Migueles and colleagues (JMPB 2019),
and van Hees and colleagues (JApplPhysiol 2014; PLoSONE 2015). The package
has been developed and tested for binary data from 'GENEActiv'
<https://activinsights.com/>, binary (.gt3x) and .csv-export data from
'Actigraph' <https://theactigraph.com> devices, and binary (.cwa) and
.csv-export data from 'Axivity' <https://axivity.com>. These devices are
currently widely used in research on human daily physical activity.
Further, the package can handle accelerometer data file from any other
sensor brand providing that the data is stored in csv format. Also the
package allows for external function embedding.

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
