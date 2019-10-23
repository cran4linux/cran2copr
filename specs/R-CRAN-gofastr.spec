%global packname  gofastr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Fast DocumentTermMatrix and TermDocumentMatrix Creation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.5
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-data.table >= 1.9.5
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-SnowballC 
Requires:         R-stats 
Requires:         R-CRAN-tm 

%description
Harness the power of 'quanteda', 'data.table' & 'stringi' to quickly
generate 'tm' DocumentTermMatrix and TermDocumentMatrix data structures.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
