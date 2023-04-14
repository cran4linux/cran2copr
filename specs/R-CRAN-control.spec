%global __brp_check_rpaths %{nil}
%global packname  control
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          A Control Systems Toolbox

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-signal 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-stats 

%description
Solves control systems problems relating to time/frequency response, LTI
systems design and analysis, transfer function manipulations, and system
conversion.

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
