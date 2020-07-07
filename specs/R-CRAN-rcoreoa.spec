%global packname  rcoreoa
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Client for the CORE API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-pdftools >= 1.3
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-hoardr 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-pdftools >= 1.3
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-hoardr 

%description
Client for the CORE API (<https://core.ac.uk/docs/>). CORE
(<https://core.ac.uk>) aggregates open access research outputs from
repositories and journals worldwide and make them available to the public.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
