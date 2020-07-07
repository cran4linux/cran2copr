%global packname  ahp
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          3%{?dist}
Summary:          Analytic Hierarchy Process

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-utils 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-DiagrammeR 

%description
Model and analyse complex decision making problems using the Analytic
Hierarchy Process (AHP) by Thomas Saaty.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/gui
%{rlibdir}/%{packname}/INDEX
