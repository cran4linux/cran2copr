%global packname  TimeVTree
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Survival Analysis of Time Varying Coefficients Using aTree-Based Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Estimates time varying regression effects under Cox type models in
survival data using classification and regression tree. The codes in this
package were originally written in S-Plus for the paper "Survival Analysis
with Time-Varying Regression Effects Using a Tree-Based Approach," by Xu,
R. and Adak, S. (2002) <doi:10.1111/j.0006-341X.2002.00305.x>, Biometrics,
58: 305-315. Development of this package was supported by NIH grants
AG053983 and AG057707, and by the UCSD Altman Translational Research
Institute, NIH grant UL1TR001442. The content is solely the responsibility
of the authors and does not necessarily represent the official views of
the NIH. The example data are from the Honolulu Heart Program/Honolulu
Asia Aging Study (HHP/HAAS).

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
%{rlibdir}/%{packname}/INDEX
