%global __brp_check_rpaths %{nil}
%global packname  gridBase
%global packver   0.4-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          3%{?dist}%{?buildtag}
Summary:          Integration of base and grid graphics

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
Requires:         R-graphics 
Requires:         R-grid 

%description
Integration of base and grid graphics

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
