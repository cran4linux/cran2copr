%global __brp_check_rpaths %{nil}
%global packname  carrier
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Isolate Functions for Remote Execution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-pryr 
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-pryr 

%description
Sending functions to remote processes can be wasteful of resources because
they carry their environments with them. With the carrier package, it is
easy to create functions that are isolated from their environment. These
isolated functions, also called crates, print at the console with their
total size and can be easily tested locally before being sent to a remote.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
