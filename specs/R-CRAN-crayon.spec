%global packname  crayon
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          2%{?dist}
Summary:          Colored Terminal Output

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 

%description
Colored terminal output on terminals that support 'ANSI' color and
highlight codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is
automatically detected. Colors and highlighting can be combined and
nested. New styles can also be created easily. This package was inspired
by the 'chalk' 'JavaScript' project.

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
%doc %{rlibdir}/%{packname}/ANSI-256-OSX.png
%doc %{rlibdir}/%{packname}/ANSI-8-OSX.png
%doc %{rlibdir}/%{packname}/logo.png
%doc %{rlibdir}/%{packname}/logo.svg.gz
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.markdown
%{rlibdir}/%{packname}/INDEX
