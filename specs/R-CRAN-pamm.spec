%global packname  pamm
%global packver   1.121
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.121
Release:          3%{?dist}%{?buildtag}
Summary:          Power Analysis for Random Effects in Mixed Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-lattice 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lme4 

%description
Simulation functions to assess or explore the power of a dataset to
estimates significant random effects (intercept or slope) in a mixed
model. The functions are based on the "lme4" and "lmerTest" packages.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
