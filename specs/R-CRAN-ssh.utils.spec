%global packname  ssh.utils
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Local and remote system commands with output and error capture.

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringr 

%description
This package provides utility functions for system command execution, both
locally and remotely using ssh/scp. The command output is captured and
provided to the caller. This functionality is intended to streamline
calling shell commands from R, retrieving and using their output, while
instrumenting the calls with appropriate error handling. NOTE: this first
version is limited to unix with local and remote systems running bash as
the default shell.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/genpdfdoc.sh
%doc %{rlibdir}/%{packname}/myfile.csv
%doc %{rlibdir}/%{packname}/ssh.utils_1.0.pdf
%{rlibdir}/%{packname}/INDEX
