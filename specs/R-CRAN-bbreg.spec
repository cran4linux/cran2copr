%global packname  bbreg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Bessel and Beta Regressions via Expectation-MaximizationAlgorithm for Continuous Bounded Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-statmod 

%description
Functions to fit, via Expectation-Maximization (EM) algorithm, the Bessel
and Beta regressions to a data set with a bounded continuous response
variable. The Bessel regression is a new and robust approach proposed in
the literature. The EM version for the well known Beta regression is
another major contribution of this package. See the reference
Barreto-Souza, Mayrink and Simas (2020) <arXiv:2003.05157> for details.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
