%global packname  R2MLwiN
%global packver   0.8-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.6
Release:          1%{?dist}
Summary:          Running 'MLwiN' from Within R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-foreign >= 0.8.46
BuildRequires:    R-CRAN-digest >= 0.6.5
BuildRequires:    R-CRAN-coda >= 0.16.1
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R2WinBUGS 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-foreign >= 0.8.46
Requires:         R-CRAN-digest >= 0.6.5
Requires:         R-CRAN-coda >= 0.16.1
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-memisc 
Requires:         R-Matrix 
Requires:         R-CRAN-R2WinBUGS 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
An R command interface to the 'MLwiN' multilevel modelling software
package.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
