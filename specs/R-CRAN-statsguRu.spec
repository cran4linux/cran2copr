%global packname  statsguRu
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Extract, Visualize and Analyze Cricket Statistics fromESPNCricinfo's Statsguru

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltab 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmltab 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-devtools 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
Use this package to scrap Test Matches, One Day Internationals, Twenty-20
Internationals data of a player from ESPNCricinfo's Statsguru
(<http://stats.espncricinfo.com/ci/engine/stats/index.html>) and then
visualize their batting, bowling and fielding performances in the form of
charts and graphs.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
