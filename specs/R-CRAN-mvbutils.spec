%global packname  mvbutils
%global packver   2.8.232
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.232
Release:          3%{?dist}
Summary:          Workspace Organization, Code and Documentation Editing, PackagePrep and Editing, Etc

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-graphics 

%description
Hierarchical workspace tree, code editing and backup, easy package prep,
editing of packages while loaded, per-object lazy-loading, easy
documentation, macro functions, and miscellaneous utilities. Needed by
debug package.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/changes.txt
%doc %{rlibdir}/%{packname}/demostuff
%{rlibdir}/%{packname}/INDEX
