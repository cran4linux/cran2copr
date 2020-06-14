%global packname  alterryx
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          An 'API' Client for the 'Alteryx' Gallery

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-base64enc 

%description
A tool to access each of the 'Alteryx' Gallery 'API' endpoints. Users can
queue jobs, poll job status, and retrieve application output as a data
frame. You will need an 'Alteryx' Server license and have 'Alteryx'
Gallery running to utilize this package. The 'API' is accessed through the
'URL' that you setup for the server running 'Alteryx' Gallery and more
information on the endpoints can be found at
<https://gallery.alteryx.com/api-docs/>.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
