%global packname  plsVarSel
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          2%{?dist}
Summary:          Variable Selection in Partial Least Squares

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MSQC 
BuildRequires:    R-CRAN-praznik 
Requires:         R-CRAN-pls 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-MASS 
Requires:         R-CRAN-progress 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-MSQC 
Requires:         R-CRAN-praznik 

%description
Interfaces and methods for variable selection in Partial Least Squares.
The methods include filter methods, wrapper methods and embedded methods.
Both regression and classification is supported.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
