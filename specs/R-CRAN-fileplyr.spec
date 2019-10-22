%global packname  fileplyr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Chunk Processing or Split-Apply-Combine on Delimited Files andDistributed Dataframes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-datadr >= 0.8.6
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-datadr >= 0.8.6
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-utils 
Requires:         R-parallel 

%description
Perform chunk processing or split-apply-combine on data in a delimited
file (example: CSV) and Distributed Dataframes (DDF) across multiple cores
of a single machine with low memory footprint. These functions are a
convenient wrapper over the versatile package 'datadr'.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
