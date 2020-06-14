%global packname  domino
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          R Console Bindings for the 'Domino Command-Line Client'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-utils 
Requires:         R-grDevices 

%description
A wrapper on top of the 'Domino Command-Line Client'. It lets you run
'Domino' commands (e.g., "run", "upload", "download") directly from your R
environment. Under the hood, it uses R's system function to run the
'Domino' executable, which must be installed as a prerequisite. 'Domino'
is a service that makes it easy to run your code on scalable hardware,
with integrated version control and collaboration features designed for
analytical workflows (see <http://www.dominodatalab.com> for more
information).

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
