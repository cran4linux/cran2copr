%global packname  ROI.plugin.neos
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          'NEOS' Plug-in for the 'R' Optimization Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xmlrpc2 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-xmlrpc2 
Requires:         R-CRAN-xml2 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package with a
connection to the 'neos' server. 'ROI' optimization problems can be
directly be sent to the 'neos' server and solution obtained in the typical
'ROI' style.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
