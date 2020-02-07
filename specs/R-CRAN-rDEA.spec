%global packname  rDEA
%global packver   1.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          Robust Data Envelopment Analysis (DEA) for R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    glpk-devel >= 4.52
Requires:         glpk
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-truncnorm >= 1.0.7
BuildRequires:    R-CRAN-truncreg >= 0.2.1
BuildRequires:    R-CRAN-slam >= 0.1.9
BuildRequires:    R-CRAN-maxLik 
Requires:         R-CRAN-truncnorm >= 1.0.7
Requires:         R-CRAN-truncreg >= 0.2.1
Requires:         R-CRAN-slam >= 0.1.9
Requires:         R-CRAN-maxLik 

%description
Data Envelopment Analysis for R, estimating robust DEA scores without and
with environmental variables and doing returns-to-scale tests.

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
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
