%global packname  ChainLadder
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          2%{?dist}
Summary:          Statistical Methods and Models for Claims Reserving in GeneralInsurance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cplm >= 0.7.3
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tweedie 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
Requires:         R-CRAN-cplm >= 0.7.3
Requires:         R-Matrix 
Requires:         R-CRAN-actuar 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-tweedie 
Requires:         R-utils 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 

%description
Various statistical methods and models which are typically used for the
estimation of outstanding claims reserves in general insurance, including
those to estimate the claims development result as required under Solvency
II.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Database
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Excel
%doc %{rlibdir}/%{packname}/Images
%doc %{rlibdir}/%{packname}/SWord
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
