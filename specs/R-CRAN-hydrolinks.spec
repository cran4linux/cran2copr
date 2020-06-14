%global packname  hydrolinks
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          2%{?dist}
Summary:          Hydrologic Network Linking Data and Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-stats 
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-httr 
Requires:         R-tools 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-units 
Requires:         R-stats 

%description
Tools to link geographic data with hydrologic network, including lakes,
streams and rivers. Includes automated download of U.S. National
Hydrography Network and other hydrolayers.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/extR
%{rlibdir}/%{packname}/INDEX
