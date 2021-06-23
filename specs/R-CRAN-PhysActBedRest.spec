%global __brp_check_rpaths %{nil}
%global packname  PhysActBedRest
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Marks Periods of 'Bedrest' in Actigraph Accelerometer Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 

%description
Contains a function to categorize accelerometer readings collected in
free-living (e.g., for 24 hours/day for 7 days), preprocessed and
compressed as counts (unit-less value) in a specified time period termed
epoch (e.g., 1 minute) as either bedrest (sleep) or active.  The input is
a matrix with a timestamp column and a column with number of counts per
epoch. The output is the same dataframe with an additional column termed
bedrest. In the bedrest column each line (epoch) contains a
function-generated classification 'br' or 'a' denoting bedrest/sleep and
activity, respectively.  The package is designed to be used after
wear/nonwear marking function in the 'PhysicalActivity' package.  Version
1.1 adds preschool thresholds and corrects for possible errors in
algorithm implementation.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
