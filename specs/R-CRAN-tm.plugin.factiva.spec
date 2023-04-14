%global __brp_check_rpaths %{nil}
%global packname  tm.plugin.factiva
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Import Articles from 'Factiva' Using the 'tm' Text MiningFramework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.7.2
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-tm >= 0.7.2
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 

%description
Provides a 'tm' Source to create corpora from articles exported from the
Dow Jones 'Factiva' content provider as XML or HTML files. It is able to
read both text content and meta-data information (including source, date,
title, author, subject, geographical coverage, company, industry, and
various provider-specific fields).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
