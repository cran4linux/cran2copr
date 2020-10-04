%global packname  morpheus
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Parameters of Mixtures of Logistic Regressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-jointDiag 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
Requires:         R-MASS 
Requires:         R-CRAN-jointDiag 
Requires:         R-methods 
Requires:         R-CRAN-pracma 

%description
Mixture of logistic regressions parameters (H)estimation with (U)spectral
methods. The main methods take d-dimensional inputs and a vector of binary
outputs, and return parameters according to the GLMs mixture model
(General Linear Model). For more details see chapter 3 in the PhD thesis
of Mor-Absa Loum: <http://www.theses.fr/s156435>, available here
<https://tel.archives-ouvertes.fr/tel-01877796/document>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
