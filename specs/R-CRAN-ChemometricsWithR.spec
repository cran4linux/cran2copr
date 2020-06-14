%global packname  ChemometricsWithR
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          2%{?dist}
Summary:          Chemometrics with R - Multivariate Data Analysis in the NaturalSciences and Life Sciences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-devtools 
Requires:         R-MASS 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-devtools 

%description
Functions and scripts used in the book "Chemometrics with R - Multivariate
Data Analysis in the Natural Sciences and Life Sciences" by Ron Wehrens,
Springer (2011). Data used in the package are available from github.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/errata.pdf
%{rlibdir}/%{packname}/INDEX
