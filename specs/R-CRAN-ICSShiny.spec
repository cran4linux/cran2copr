%global packname  ICSShiny
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          ICS via a Shiny Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ICS 
BuildRequires:    R-CRAN-ICSOutlier 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-simsalapar 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-ICS 
Requires:         R-CRAN-ICSOutlier 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-simsalapar 
Requires:         R-CRAN-DT 

%description
Performs Invariant Coordinate Selection (ICS) (Tyler, Critchley, Duembgen
and Oja (2009) <doi:10.1111/j.1467-9868.2009.00706.x>) and especially ICS
for multivariate outlier detection with application to quality control
(Archimbaud, Nordhausen, Ruiz-Gazen (2016) <arXiv:1612.06118>) using a
shiny app.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/ICSShiny
%{rlibdir}/%{packname}/INDEX
