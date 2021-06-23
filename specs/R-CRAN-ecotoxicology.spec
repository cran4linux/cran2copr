%global __brp_check_rpaths %{nil}
%global packname  ecotoxicology
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Ecotoxicology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Implementation of the EPA's Ecological Exposure Research Division (EERD)
tools (discontinued in 1999) for Probit and Trimmed Spearman-Karber
Analysis. Probit and Spearman-Karber methods from Finney's book "Probit
analysis a statistical treatment of the sigmoid response curve" with
options for most accurate results or identical results to the book. Probit
and all the tables from Finney's book (code-generated, not copied) with
the generating functions included. Control correction: Abbott,
Schneider-Orelli, Henderson-Tilton, Sun-Shepard. Toxicity scales:
Horsfall-Barratt, Archer, Gauhl-Stover, Fullerton-Olsen, etc.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
