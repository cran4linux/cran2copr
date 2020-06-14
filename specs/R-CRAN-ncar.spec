%global packname  ncar
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}
Summary:          Noncompartmental Analysis for Pharmacokinetic Report

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-NonCompart >= 0.3.3
BuildRequires:    R-CRAN-rtf 
Requires:         R-CRAN-NonCompart >= 0.3.3
Requires:         R-CRAN-rtf 

%description
Conduct a noncompartmental analysis with industrial strength. Some
features are 1) CDISC SDTM terms 2) Automatic or manual slope selection 3)
Supporting both 'linear-up linear-down' and 'linear-up log-down' method 4)
Interval(partial) AUCs with 'linear' or 'log' interpolation method 5)
Produce pdf, rtf, text report files. * Reference: Gabrielsson J, Weiner D.
Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and
Applications. 5th ed. 2016. (ISBN:9198299107).

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
