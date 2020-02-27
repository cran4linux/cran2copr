%global packname  vcrpart
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Tree-Based Varying Coefficient Regression for Generalized Linearand Ordinal Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-nlme >= 3.1.123
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-nlme >= 3.1.123
Requires:         R-parallel 
Requires:         R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-rpart 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-strucchange 

%description
Recursive partitioning for varying coefficient generalized linear models
and ordinal linear mixed models. Special features are coefficient-wise
partitioning, non-varying coefficients and partitioning of time-varying
variables in longitudinal regression.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
