%global __brp_check_rpaths %{nil}
%global packname  RSEIS
%global packver   3.9-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Seismic Time Series Analysis Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-Rwave 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-Rwave 

%description
Multiple interactive codes to view and analyze seismic data, via spectrum
analysis, wavelet transforms, particle motion, hodograms.  Includes
general time-series tools, plotting, filtering, interactive display.

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
