%global packname  theiaR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Download and Manage Data from Theia

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.86
BuildRequires:    R-tools >= 3.5
BuildRequires:    R-CRAN-raster >= 2.6
BuildRequires:    R-CRAN-R6 >= 2.3
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-askpass >= 1.1
Requires:         R-CRAN-XML >= 3.86
Requires:         R-tools >= 3.5
Requires:         R-CRAN-raster >= 2.6
Requires:         R-CRAN-R6 >= 2.3
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-askpass >= 1.1

%description
Provides a simple interface to search available data provided by Theia
(<https://theia.cnes.fr>), download it, and manage it. Data can be
downloaded based on a search result or from a cart file downloaded from
Theia website.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
