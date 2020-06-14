%global packname  targeted
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Targeted Inference

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-lava >= 1.6.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lava >= 1.6.6
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-futile.logger 

%description
Various methods for targeted and semiparametric inference including
augmented inverse probability weighted estimators for missing data and
causal inference (Bang and Robins (2005)
<doi:10.1111/j.1541-0420.2005.00377.x>) and estimators for risk
differences and relative risks (Richardson et al. (2017)
<doi:10.1080/01621459.2016.1192546>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
