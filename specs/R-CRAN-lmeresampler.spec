%global packname  lmeresampler
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Bootstrap Methods for Nested Linear Mixed-Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-nlmeU 
BuildRequires:    R-CRAN-RLRsim 
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-boot 
Requires:         R-CRAN-plyr 
Requires:         R-Matrix 
Requires:         R-CRAN-nlmeU 
Requires:         R-CRAN-RLRsim 

%description
Bootstrap routines for nested linear mixed effects models fit using either
'lme4' or 'nlme'. The provided 'bootstrap()' function implements the
parametric, residual, cases, semi-parametric (i.e., CGR), and random
effect block (REB) bootstrap procedures. An overview of these procedures
can be found in Van der Leeden et al. (2008) <doi:
10.1007/978-0-387-73186-5_11>, Carpenter, Goldstein & Rasbash (2003) <doi:
10.1111/1467-9876.00415>, and Chambers & Chandra (2013) <doi:
10.1080/10618600.2012.681216>.

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
%{rlibdir}/%{packname}/INDEX
