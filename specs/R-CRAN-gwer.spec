%global packname  gwer
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Geographically Weighted Elliptical Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 0.8.3
BuildRequires:    R-CRAN-maptools >= 0.7.32
BuildRequires:    R-CRAN-spData >= 0.2.6.2
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-spgwr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glogis 
BuildRequires:    R-graphics 
Requires:         R-CRAN-sp >= 0.8.3
Requires:         R-CRAN-maptools >= 0.7.32
Requires:         R-CRAN-spData >= 0.2.6.2
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-spgwr 
Requires:         R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glogis 
Requires:         R-graphics 

%description
Computes a elliptical regression model or a geographically weighted
regression model with elliptical errors using Fisher's score algorithm.
Provides diagnostic measures, residuals and analysis of variance.
Cysneiros, F. J. A., Paula, G. A., and Galea, M. (2007)
<doi:10.1016/j.spl.2007.01.012>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
