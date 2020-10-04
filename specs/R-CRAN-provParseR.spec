%global packname  provParseR
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Pulls Information from Prov.Json Files

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 

%description
R functions to access provenance information collected by 'rdt' or
'rdtLite'.  The information is stored inside a 'ProvInfo' object and can
be accessed through a collection of functions that will return the
requested data. The exact format of the JSON created by 'rdt' and
'rdtLite' is described in
<https://github.com/End-to-end-provenance/ExtendedProvJson>.

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
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/testexpected
%doc %{rlibdir}/%{packname}/testscripts
%{rlibdir}/%{packname}/INDEX
