%global __brp_check_rpaths %{nil}
%global packname  metRology
%global packver   0.9-28-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.28.1
Release:          3%{?dist}%{?buildtag}
Summary:          Support for Metrological Applications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-robustbase 

%description
Provides classes and calculation and plotting functions for metrology
applications, including measurement uncertainty estimation and
inter-laboratory metrology comparison studies.

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
