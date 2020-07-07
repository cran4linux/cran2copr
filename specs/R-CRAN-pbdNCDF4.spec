%global packname  pbdNCDF4
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Programming with Big Data -- Interface to Parallel UnidataNetCDF4 Format Data Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel >= 1.5.4
BuildRequires:    netcdf-devel >= 4.1
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
This package adds collective parallel read and write capability to the R
package ncdf4 version 1.8. Typical use is as a parallel NetCDF4 file
reader in SPMD style programming. Each R process reads and writes its own
data in a synchronized collective mode, resulting in faster parallel
performance. Performance improvement is conditional on a parallel file
system.

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

%files
%{rlibdir}/%{packname}
