%global packname  LSC
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Local Statistical Complexity - Automatic Pattern Discovery inSpatio-Temporal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-LICORS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-LICORS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gam 
Requires:         R-Matrix 

%description
Estimators and visualization for local statistical complexity of (N+1)D
fields. In particular for 0, 1 and 2 dimensional space this package
provides useful visualization.

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
