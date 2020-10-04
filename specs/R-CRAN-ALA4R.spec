%global packname  ALA4R
%global packver   1.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          Atlas of Living Australia (ALA) Data and Resources in R

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.8
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-wellknown 
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.8
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-wellknown 

%description
The Atlas of Living Australia (ALA) provides tools to enable users of
biodiversity information to find, access, combine and visualise data on
Australian plants and animals; these have been made available from
<https://ala.org.au/>. ALA4R provides a subset of the tools to be directly
used within R. It enables the R community to directly access data and
resources hosted by the ALA.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
