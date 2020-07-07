%global packname  chromoR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Analysis of chromosomal interactions data (correction,segmentation and comparison)

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-CRAN-haarfisz 
BuildRequires:    R-CRAN-gdata 
Requires:         R-CRAN-haarfisz 
Requires:         R-CRAN-gdata 

%description
chromoR provides users with a statistical pipeline for analysing
chromosomal interactions data (Hi-C data).It combines wavelet methods and
a Bayesian approach for correction (bias and noise) and comparison
(detecting significant changes between Hi-C maps) of Hi-C contact maps.In
addition, it also support detection of change points in 1D Hi-C contact
profiles.

%prep
%setup -q -c -n %{packname}
find %{packname}/exec -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;

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
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
