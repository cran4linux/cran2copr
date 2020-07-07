%global packname  STB
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          2%{?dist}
Summary:          Simultaneous Tolerance Bounds

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-VCA >= 1.3.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-VCA >= 1.3.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 

%description
Provides an implementation of simultaneous tolerance bounds (STB), useful
for checking whether a numeric vector fits to a hypothetical
null-distribution or not. Furthermore, there are functions for computing
STB (bands, intervals) for random variates of linear mixed models fitted
with package 'VCA'. All kinds of, possibly transformed (studentized,
standardized, Pearson-type transformed) random variates (residuals, random
effects), can be assessed employing STB-methodology.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/ChangeLog.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
