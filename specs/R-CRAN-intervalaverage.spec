%global packname  intervalaverage
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Time-Weighted Averaging for Interval Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-Rcpp 

%description
Perform fast and memory efficient time-weighted averaging of values
measured over intervals into new arbitrary intervals. This package is
useful in the context of data measured or represented as constant values
over intervals on a one-dimensional discrete axis (e.g. time-integrated
averages of a curve over defined periods). This package was written
specifically to deal with air pollution data recorded or predicted as
averages over sampling periods. Data in this format often needs to be
shifted to non-aligned periods or averaged up to periods of longer
duration (e.g. averaging data measured over sequential non-overlapping
periods to calendar years).

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
