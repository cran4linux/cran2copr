%global packname  librarian
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          2%{?dist}
Summary:          Install, Update, Load Packages from CRAN, 'GitHub', and'Bioconductor' in One Step

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-remotes 
Requires:         R-tools 
Requires:         R-utils 

%description
Automatically install, update, and load 'CRAN', 'GitHub', and
'Bioconductor' packages in a single function call. By accepting bare
unquoted names for packages, it's easy to add or remove packages from the
list.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
