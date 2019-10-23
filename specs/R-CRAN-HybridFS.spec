%global packname  HybridFS
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          A Hybrid Filter-Wrapper Feature Selection Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-woeBinning 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-InformationValue 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-woeBinning 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-InformationValue 

%description
A hybrid method of feature selection which combines both filter and
wrapper methods. The first level involves feature reduction based on some
of the important filter methods while the second level involves feature
subset selection as in a wrapper method. Comparative analysis with the
existing feature selection packages shows this package results in higher
classification accuracy, reduced processing time and improved data
handling capacity.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
