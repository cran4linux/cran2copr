%global packname  Iso
%global packver   0.0-18.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.18.1
Release:          1%{?dist}
Summary:          Functions to Perform Isotonic Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7.0
Requires:         R-core >= 1.7.0

%description
Linear order and unimodal order (univariate) isotonic regression;
bivariate isotonic regression with linear order on both variables.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/draft0.tex
%doc %{rlibdir}/%{packname}/Isotonic.for
%doc %{rlibdir}/%{packname}/makefor
%doc %{rlibdir}/%{packname}/pava.r
%doc %{rlibdir}/%{packname}/smooth.f.orig
%doc %{rlibdir}/%{packname}/ufit.r
%doc %{rlibdir}/%{packname}/unimode.r
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
