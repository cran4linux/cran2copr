%global packname  REPPlab
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          R Interface to 'EPP-Lab', a Java Program for ExploratoryProjection Pursuit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-LDRTools >= 0.2
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-lattice 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-LDRTools >= 0.2
Requires:         R-CRAN-rJava 
Requires:         R-lattice 
Requires:         R-utils 
Requires:         R-graphics 

%description
An R Interface to 'EPP-lab' v1.0. 'EPP-lab' is a Java program for
projection pursuit using genetic algorithms written by Alain Berro and S.
Larabi Marie-Sainte and is included in the package. The 'EPP-lab' sources
are available under https://github.com/fischuu/EPP-lab.git.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
