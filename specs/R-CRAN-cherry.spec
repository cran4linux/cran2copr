%global packname  cherry
%global packver   0.6-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.13
Release:          1%{?dist}
Summary:          Multiple Testing Methods for Exploratory Research

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-hommel 
Requires:         R-methods 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-lpSolve 
Requires:         R-Matrix 
Requires:         R-CRAN-hommel 

%description
Provides an alternative approach to multiple testing by calculating a
simultaneous upper confidence bounds for the number of true null
hypotheses among any subset of the hypotheses of interest, using the
methods of Goeman and Solari (2011) <doi:10.1214/11-STS356>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
