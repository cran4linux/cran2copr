%global __brp_check_rpaths %{nil}
%global packname  copulaedas
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of Distribution Algorithms Based on Copulas

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-vines 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-methods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-vines 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 

%description
Provides a platform where EDAs (estimation of distribution algorithms)
based on copulas can be implemented and studied. The package offers
complete implementations of various EDAs based on copulas and vines, a
group of well-known optimization problems, and utility functions to study
the performance of the algorithms. Newly developed EDAs can be easily
integrated into the package by extending an S4 class with generic
functions for their main components.

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
