%global packname  tvReg
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Time-Varying Coefficient Linear Regression for Single andMulti-Equations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats >= 2.14.0
BuildRequires:    R-CRAN-systemfit >= 1.1.20
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-bvarsv 
Requires:         R-stats >= 2.14.0
Requires:         R-CRAN-systemfit >= 1.1.20
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-plm 
Requires:         R-MASS 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-bvarsv 

%description
Fitting time-varying coefficient models both for single and multi-equation
regressions, using kernel smoothing techniques.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
