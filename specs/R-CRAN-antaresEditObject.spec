%global packname  antaresEditObject
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          2%{?dist}
Summary:          Edit an 'Antares' Simulation

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-antaresRead 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-antaresRead 
Requires:         R-CRAN-assertthat 
Requires:         R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-whisker 

%description
Edit an 'Antares' simulation before running it : create new areas, links,
thermal clusters or binding constraints or edit existing ones. Update
'Antares' general & optimization settings. 'Antares' is an open source
power system generator, more information available here :
<https://antares-simulator.org/>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/newStudy
%doc %{rlibdir}/%{packname}/template-antares
%{rlibdir}/%{packname}/INDEX
