%global packname  ImputeRobust
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}
Summary:          Robust Multiple Imputation with Generalized Additive Models forLocation Scale and Shape

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-extremevalues 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-lattice 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-extremevalues 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-lattice 

%description
Provides new imputation methods for the 'mice' package based on
generalized additive models for location, scale, and shape (GAMLSS) as
described in de Jong, van Buuren and Spiess
<doi:10.1080/03610918.2014.911894>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
