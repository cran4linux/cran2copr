%global packname  dcmodify
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Modify Data Using Externally Defined Modification Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-validate >= 0.1.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-utils 
Requires:         R-CRAN-validate >= 0.1.5
Requires:         R-methods 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-settings 
Requires:         R-utils 

%description
Data cleaning scripts typically contain a lot of 'if this change that'
type of statements. Such statements are typically condensed expert
knowledge. With this package, such 'data modifying rules' are taken out of
the code and become in stead parameters to the work flow. This allows one
to maintain, document, and reason about data modification rules as
separate entities.

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
%{rlibdir}/%{packname}/INDEX
