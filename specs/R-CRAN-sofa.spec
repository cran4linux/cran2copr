%global packname  sofa
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}%{?buildtag}
Summary:          Connector to 'CouchDB'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-mime 

%description
Provides an interface to the 'NoSQL' database 'CouchDB'
(<http://couchdb.apache.org>). Methods are provided for managing databases
within 'CouchDB', including creating/deleting/updating/transferring, and
managing documents within databases. One can connect with a local
'CouchDB' instance, or a remote 'CouchDB' databases such as 'Cloudant'.
Documents can be inserted directly from vectors, lists, data.frames, and
'JSON'. Targeted at 'CouchDB' v2 or greater.

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
