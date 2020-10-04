%global packname  nFactors
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          2%{?dist}%{?buildtag}
Summary:          Parallel Analysis and Other Non Graphical Solutions to theCattell Scree Test

License:          GPL (>= 3.5.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-psych 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-psych 

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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
