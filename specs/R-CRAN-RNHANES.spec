%global __brp_check_rpaths %{nil}
%global packname  RNHANES
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Facilitates Analysis of CDC NHANES Data

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-foreign 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 

%description
Tools for downloading and analyzing CDC NHANES data, with a focus on
analytical laboratory data.

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
