%global __brp_check_rpaths %{nil}
%global packname  behavr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Canonical Data Structure for Behavioural Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
Implements an S3 class based on 'data.table' to store and process
efficiently ethomics (high-throughput behavioural) data.

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
