%global packname  MMS
%global packver   3.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.11
Release:          1%{?dist}
Summary:          Fixed Effects Selection in Linear Mixed Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mht >= 3.00
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-mht >= 3.00
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 

%description
Perform Fixed effects Selection in Linear Mixed Models using a multicycle
ECM algorithm; see F. Rohart & al, 2014, <doi:10.1016/j.csda.2014.06.022>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
