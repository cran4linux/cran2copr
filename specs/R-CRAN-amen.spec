%global packname  amen
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Additive and Multiplicative Effects Models for Networks andRelational Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Analysis of dyadic network and relational data using additive and
multiplicative effects (AME) models. The basic model includes regression
terms, the covariance structure of the social relations model (Warner,
Kenny and Stoto (1979) <DOI:10.1037/0022-3514.37.10.1742>, Wong (1982)
<DOI:10.2307/2287296>), and multiplicative factor models (Hoff(2009)
<DOI:10.1007/s10588-008-9040-4>). Four different link functions
accommodate different relational data structures, including binary/network
data (bin), normal relational data (nrm), ordinal relational data (ord)
and data from fixed-rank nomination schemes (frn).  Several of these link
functions are discussed in Hoff, Fosdick, Volfovsky and Stovel (2013)
<DOI:10.1017/nws.2013.17>. Development of this software was supported in
part by NIH grant R01HD067509.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
