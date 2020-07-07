%global packname  robustrank
%global packver   2019.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.3.7
Release:          3%{?dist}
Summary:          Robust Rank-Based Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-kyotil 
Requires:         R-CRAN-kyotil 

%description
Implements two-sample tests for paired data with missing values (Fong,
Huang, Lemos and McElrath 2018, Biostatics,
<doi:10.1093/biostatistics/kxx039>) and modified Wilcoxon-Mann-Whitney two
sample location test, also known as the Fligner-Policello test.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
