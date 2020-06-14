%global packname  textir
%global packver   2.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          2%{?dist}
Summary:          Inverse Regression for Text Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-distrom 
BuildRequires:    R-CRAN-gamlr 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-distrom 
Requires:         R-CRAN-gamlr 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Multinomial (inverse) regression inference for text documents and
associated attributes.  For details see: Taddy (2013 JASA) Multinomial
Inverse Regression for Text Analysis <arXiv:1012.2098> and Taddy (2015,
AoAS), Distributed Multinomial Regression, <arXiv:1311.6139>. A minimalist
partial least squares routine is also included.  Note that the topic
modeling capability of earlier 'textir' is now a separate package,
'maptpx'.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
