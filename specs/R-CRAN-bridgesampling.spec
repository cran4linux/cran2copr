%global packname  bridgesampling
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Bridge Sampling for Marginal Likelihoods and Bayes Factors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-methods 

%description
Provides functions for estimating marginal likelihoods, Bayes factors,
posterior model probabilities, and normalizing constants in general, via
different versions of bridge sampling (Meng & Wong, 1996,
<http://www3.stat.sinica.edu.tw/statistica/j6n4/j6n43/j6n43.htm>). Gronau,
Singmann, & Wagenmakers (2020) <doi:10.18637/jss.v092.i10>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
