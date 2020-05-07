%global packname  datapackage.r
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Data Package 'Frictionless Data'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tableschema.r 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-V8 
Requires:         R-CRAN-config 
Requires:         R-CRAN-future 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tableschema.r 
Requires:         R-tools 
Requires:         R-CRAN-urltools 
Requires:         R-utils 
Requires:         R-CRAN-V8 

%description
Work with 'Frictionless Data Packages'
(<https://frictionlessdata.io/specs/data-package/>). Allows to load and
validate any descriptor for a data package profile, create and modify
descriptors and provides expose methods for reading and streaming data in
the package. When a descriptor is a 'Tabular Data Package', it uses the
'Table Schema' package
(<https://CRAN.R-project.org/package=tableschema.r>) and exposes its
functionality, for each resource object in the resources field.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/config
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/profiles
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
