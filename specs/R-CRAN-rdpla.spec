%global packname  rdpla
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Client for the Digital Public Library of America ('DPLA')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-crul >= 0.3.8
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hoardr 
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-crul >= 0.3.8
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hoardr 

%description
Interact with the Digital Public Library of America <https://dp.la>
('DPLA') 'REST' 'API' <https://dp.la/info/developers/codex/> from R,
including search and more.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
