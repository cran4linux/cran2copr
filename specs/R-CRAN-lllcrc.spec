%global packname  lllcrc
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Local Log-linear Models for Capture-Recapture

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-plyr 

%description
Applies local log-linear capture-recapture models (LLLMs) for closed
populations, as described in the doctoral thesis of Zachary Kurtz. The
method is relevant when there are 3-5 capture occasions, with auxiliary
covariates available for all capture occasions.  As part of estimating the
number of missing population units, the method estimates the "rate of
missingness" as it varies over the covariate space.  In addition,
user-friendly functions are provided to recreate (approximately) the
method of Zwane and van der Heijden (2004), which applied the VGAM package
in a way that is closely related to LLLMs.

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
%{rlibdir}/%{packname}/INDEX
