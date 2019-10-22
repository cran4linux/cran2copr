%global packname  popRange
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          popRange: A spatially and temporally explicit forward geneticsimulator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3dist(numpy)
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-findpython 
Requires:         R-CRAN-findpython 

%description
Runs a forward genetic simulator

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
%doc %{rlibdir}/%{packname}/__pycache__
%doc %{rlibdir}/%{packname}/config_3.py
%doc %{rlibdir}/%{packname}/config_old.py
%doc %{rlibdir}/%{packname}/config.py
%doc %{rlibdir}/%{packname}/popRange_main_3.py
%doc %{rlibdir}/%{packname}/popRange_main.py
%doc %{rlibdir}/%{packname}/setup_program_3.py
%doc %{rlibdir}/%{packname}/setup_program.py
%doc %{rlibdir}/%{packname}/writeOutput_3.py
%doc %{rlibdir}/%{packname}/writeOutput.py
%{rlibdir}/%{packname}/INDEX
