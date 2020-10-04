%global packname  pkr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Pharmacokinetics in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-rtf 
Requires:         R-foreign 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-rtf 

%description
Conduct a noncompartmental analysis as closely as possible to the most
widely used commercial software for pharmacokinetic analysis, i.e.
'Phoenix(R) WinNonlin(R)'
<https://www.certara.com/software/pkpd-modeling-and-simulation/phoenix-winnonlin/>.
Some features are 1) CDISC SDTM terms 2) Automatic slope selection with
the same criterion of WinNonlin(R) 3) Supporting both 'linear-up
linear-down' and 'linear-up log-down' method 4) Interval(partial) AUCs
with 'linear' or 'log' interpolation method * Reference: Gabrielsson J,
Weiner D. Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and
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
