%global packname  nFactors
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}
Summary:          Parallel Analysis and Non Graphical Solutions to the CattellScree Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-boot 
BuildRequires:    R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-psych 
Requires:         R-boot 
Requires:         R-lattice 

%description
Indices, heuristics and strategies to help determine the number of
factors/components to retain: 1. Acceleration factor (af with or without
Parallel Analysis); 2. Optimal Coordinates (noc with or without Parallel
Analysis); 3. Parallel analysis (components, factors and bootstrap); 4.
lambda > mean(lambda) (Kaiser, CFA and related); 5. Cattell-Nelson-Gorsuch
(CNG); 6. Zoski and Jurs multiple regression (b, t and p); 7. Zoski and
Jurs standard error of the regression coeffcient (sescree); 8. Nelson R2;
9. Bartlett khi-2; 10. Anderson khi-2; 11. Lawley khi-2 and 12.
Bentler-Yuan khi-2.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
