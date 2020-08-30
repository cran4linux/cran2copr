%global packname  neonstore
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          NEON Data Store

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-vroom 
Requires:         R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-digest 

%description
The National Ecological Observatory Network (NEON) provides access to its
numerous data products through its REST API,
<https://data.neonscience.org/data-api/>. This package provides a
high-level user interface for downloading and storing NEON data products.
While each of NEON data products consist of hundreds or thousands of
individual files.  Unlike 'neonUtilities', this package will avoid
repeated downloading, provides persistent storage, and improves
performance.  This package does not provide expose interactions with the
individual low-level NEON API endpoints.

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
