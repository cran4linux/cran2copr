%global packname  dcmle
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Hierarchical Models Made Easy with Data Cloning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dclone >= 2.0.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-lattice 
Requires:         R-CRAN-dclone >= 2.0.0
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-lattice 

%description
S4 classes around infrastructure provided by the 'coda' and 'dclone'
packages to make package development easy as a breeze with data cloning
for hierarchical models.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
