%global __brp_check_rpaths %{nil}
%global packname  frair
%global packver   0.5.100
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.100
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Functional Response Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lamW >= 1.0
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
Requires:         R-CRAN-lamW >= 1.0
Requires:         R-stats4 
Requires:         R-CRAN-bbmle 
Requires:         R-boot 
Requires:         R-parallel 

%description
Tools to support sensible statistics for functional response analysis.

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
