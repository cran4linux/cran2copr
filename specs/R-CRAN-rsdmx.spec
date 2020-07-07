%global packname  rsdmx
%global packver   0.5-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.14
Release:          3%{?dist}
Summary:          Tools for Reading SDMX Data and Metadata

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-XML >= 3.98.1.3
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-plyr 
Requires:         R-utils 

%description
Set of classes and methods to read data and metadata documents exchanged
through the Statistical Data and Metadata Exchange (SDMX) framework,
currently focusing on the SDMX XML standard format (SDMX-ML).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
