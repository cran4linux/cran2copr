%global packname  RcmdrPlugin.EBM
%global packver   1.0-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}
Summary:          Rcmdr Evidence Based Medicine Plug-in Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.7.0
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-Rcmdr >= 1.7.0
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-abind 

%description
Rcmdr plug-in GUI extension for Evidence Based Medicine medical indicators
calculations (Sensitivity, specificity, absolute risk reduction, relative
risk, ...).

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
