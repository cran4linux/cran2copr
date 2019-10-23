%global packname  replyr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Patches to Use 'dplyr' on Remote Data Sources

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 1.8.8
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-DBI 
Requires:         R-CRAN-wrapr >= 1.8.8
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-DBI 

%description
Patches to use 'dplyr' on remote data sources ('SQL' databases, 'Spark'
2.0.0 and above) in a reliable "generic" fashion (generic meaning user
code works similarly on all such sources, without needing per-source
adaption).  Due to the fluctuating nature of 'dplyr'/'dbplyr'/'rlang'
'APIs' this package is going into maintenance mode.  Most of the 'replyr'
functions are already done better by one of the non-monolithic replacement
packages: 'wrapr', 'seplyr', 'rquery', or 'cdata'.

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
