%global packname  mpoly
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Symbolic Computation and More with Multivariate Polynomials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-tidyr 

%description
Symbolic computing with multivariate polynomials in R.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
