%global __brp_check_rpaths %{nil}
%global packname  miscF
%global packver   0.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-MCMCpack >= 1.2.4
BuildRequires:    R-CRAN-mvtnorm >= 0.9.9992
BuildRequires:    R-CRAN-R2jags >= 0.5.7
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-MCMCpack >= 1.2.4
Requires:         R-CRAN-mvtnorm >= 0.9.9992
Requires:         R-CRAN-R2jags >= 0.5.7

%description
Various functions for random number generation, density estimation,
classification, curve fitting, and spatial data analysis.

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
