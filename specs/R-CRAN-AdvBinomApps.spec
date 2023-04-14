%global __brp_check_rpaths %{nil}
%global packname  AdvBinomApps
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Upper Clopper-Pearson Confidence Limits for Burn-in Studiesunder Additional Available Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GenBinomApps 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-GenBinomApps 
Requires:         R-CRAN-rootSolve 

%description
Functions to compute upper Clopper-Pearson confidence limits of early life
failure probabilities and required sample sizes of burn-in studies under
further available information, e.g. from other products or technologies.

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
