%global packname  personograph
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Pictographic Representation of Treatment Effects

License:          LGPL (>= 2.0, < 3) | Mozilla Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-grImport 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
Requires:         R-CRAN-grImport 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-grid 

%description
Visualizes treatment effects using person icons, similar to Cates (NNT)
charts.

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
%doc %{rlibdir}/%{packname}/1.ps.xml
%doc %{rlibdir}/%{packname}/10.ps.xml
%doc %{rlibdir}/%{packname}/11.ps.xml
%doc %{rlibdir}/%{packname}/2.ps.xml
%doc %{rlibdir}/%{packname}/3.ps.xml
%doc %{rlibdir}/%{packname}/4.ps.xml
%doc %{rlibdir}/%{packname}/5.ps.xml
%doc %{rlibdir}/%{packname}/6.ps.xml
%doc %{rlibdir}/%{packname}/7.ps.xml
%doc %{rlibdir}/%{packname}/8.ps.xml
%doc %{rlibdir}/%{packname}/9.ps.xml
%{rlibdir}/%{packname}/INDEX
