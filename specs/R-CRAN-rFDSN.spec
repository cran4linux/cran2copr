%global packname  rFDSN
%global packver   0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Get Seismic Data from the International Federation of Digital Seismograph Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.1
Requires:         R-CRAN-XML >= 3.98.1.1

%description
This package facilitates searching for and downloading seismic time series
in miniSEED format (a minimalist version of the Standard for the Exchange
of Earthquake Data) from International Federation of Digital Seismograph
Networks repositories. This package can also be used to gather information
about seismic networks (stations, channels, locations, etc) and find
historical earthquake data (origins, magnitudes, etc).

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
