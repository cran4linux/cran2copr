%global __brp_check_rpaths %{nil}
%global packname  vars
%global packver   1.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          VAR Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.2.4
BuildRequires:    R-CRAN-urca >= 1.1.6
BuildRequires:    R-CRAN-lmtest >= 0.9.26
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-CRAN-sandwich >= 2.2.4
Requires:         R-CRAN-urca >= 1.1.6
Requires:         R-CRAN-lmtest >= 0.9.26
Requires:         R-MASS 
Requires:         R-CRAN-strucchange 

%description
Estimation, lag selection, diagnostic testing, forecasting, causality
analysis, forecast error variance decomposition and impulse response
functions of VAR models and estimation of SVAR and SVEC models.

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
%doc %{rlibdir}/%{packname}/book-ex
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
