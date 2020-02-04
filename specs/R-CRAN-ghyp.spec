%global packname  ghyp
%global packver   1.5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.9
Release:          1%{?dist}
Summary:          Generalized Hyperbolic Distribution and Its Special Cases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7
Requires:         R-core >= 2.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 

%description
Detailed functionality for working with the univariate and multivariate
Generalized Hyperbolic distribution and its special cases (Hyperbolic
(hyp), Normal Inverse Gaussian (NIG), Variance Gamma (VG), skewed
Student-t and Gaussian distribution). Especially, it contains fitting
procedures, an AIC-based model selection routine, and functions for the
computation of density, quantile, probability, random variates, expected
shortfall and some portfolio optimization and plotting routines as well as
the likelihood ratio test. In addition, it contains the Generalized
Inverse Gaussian distribution. See Chapter 3 of A. J. McNeil, R. Frey, and
P. Embrechts. Quantitative risk management: Concepts, techniques and
tools. Princeton University Press, Princeton (2005).

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
%doc %{rlibdir}/%{packname}/Fixme
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
