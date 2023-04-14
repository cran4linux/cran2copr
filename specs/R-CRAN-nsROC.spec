%global __brp_check_rpaths %{nil}
%global packname  nsROC
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Standard ROC Curve Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-survival 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-sde 
Requires:         R-survival 

%description
Tools for estimating Receiver Operating Characteristic (ROC) curves,
building confidence bands, comparing several curves both for dependent and
independent data, estimating the cumulative-dynamic ROC curve in presence
of censored data, and performing meta-analysis studies, among others.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
