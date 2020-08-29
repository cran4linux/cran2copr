%global packname  ibmAcousticR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to Your 'IBM Acoustic' Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.99.0.5
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-XML >= 3.99.0.5
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.1

%description
Authentication can be the most difficult part about working with a new
API. 'ibmAcousticR' facilitates making a connection to the 'IBM Acoustic'
email campaign management API and executing various queries. The 'IBM
Acoustic' API documentation is available at
<https://developer.ibm.com/customer-engagement/docs/>. This package is not
supported by 'IBM'.

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
