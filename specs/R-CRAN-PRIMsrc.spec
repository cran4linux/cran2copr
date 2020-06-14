%global packname  PRIMsrc
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          2%{?dist}
Summary:          PRIM Survival Regression Classification

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-superpc 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-parallel 
Requires:         R-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-superpc 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-quantreg 
Requires:         R-parallel 

%description
Performs a unified treatment of Bump Hunting by Patient Rule Induction
Method (PRIM) in Survival, Regression and Classification settings (SRC).
The current version is a development release that only implements the case
of a survival response.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
