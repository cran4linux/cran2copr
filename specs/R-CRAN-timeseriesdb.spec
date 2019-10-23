%global packname  timeseriesdb
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Manage Time Series for Official Statistics with R and PostgreSQL

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-methods 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-openxlsx 

%description
Archive and manage times series data from official statistics. The
'timeseriesdb' package was designed to manage a large catalog of time
series from official statistics which are typically published on a
monthly, quarterly or yearly basis. Thus timeseriesdb is optimized to
handle updates caused by data revision as well as elaborate, multi-lingual
meta information.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/hstore_vs_flat_benchmarks.R
%{rlibdir}/%{packname}/INDEX
