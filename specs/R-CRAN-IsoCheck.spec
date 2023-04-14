%global __brp_check_rpaths %{nil}
%global packname  IsoCheck
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Isomorphism Check for Multi-Stage Factorial Designs withRandomization Restrictions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 

%description
Contains functions to check the isomorphism of multi-stage factorial
designs with randomisation restrictions based on balanced spreads and
balanced covering stars of PG(n-1,2) as described in Spencer, Ranjan and
Mendivil (2019) <doi:10.1007/s42519-019-0064-5>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
