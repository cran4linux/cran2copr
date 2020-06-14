%global packname  tlrmvnmvt
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Low-Rank Methods for MVN and MVT Probabilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Implementation of the classic Genz algorithm and a novel tile-low-rank
algorithm for computing relatively high-dimensional multivariate normal
(MVN) and Student-t (MVT) probabilities. References used for this package:
Foley, James, Andries van Dam, Steven Feiner, and John Hughes. "Computer
Graphics: Principle and Practice". Addison-Wesley Publishing Company.
Reading, Massachusetts (1987, ISBN:0-201-84840-6 1); Genz, A., "Numerical
computation of multivariate normal probabilities," Journal of
Computational and Graphical Statistics, 1, 141-149 (1992)
<doi:10.1080/10618600.1992.10477010>; Cao, J., Genton, M. G., Keyes, D.
E., & Turkiyyah, G. M. "Exploiting Low Rank Covariance Structures for
Computing High-Dimensional Normal and Student- t Probabilities" (2019)
<https://marcgenton.github.io/2019.CGKT.manuscript.pdf>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
