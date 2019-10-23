%global packname  LTRCtrees
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Survival Trees to Fit Left-Truncated and Right-Censored andInterval-Censored Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.0
BuildRequires:    R-rpart 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-inum 
BuildRequires:    R-CRAN-icenReg 
Requires:         R-CRAN-partykit >= 1.2.0
Requires:         R-rpart 
Requires:         R-survival 
Requires:         R-CRAN-inum 
Requires:         R-CRAN-icenReg 

%description
Recursive partition algorithms designed for fitting survival tree with
left-truncated and right censored (LTRC) data, as well as
interval-censored data. The LTRC trees can also be used to fit survival
tree with time-varying covariates.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
