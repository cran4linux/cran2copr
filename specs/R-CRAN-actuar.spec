%global packname  actuar
%global packver   3.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          2%{?dist}
Summary:          Actuarial Functions and Heavy Tailed Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-expint 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-expint 

%description
Functions and data sets for actuarial science: modeling of loss
distributions; risk theory and ruin theory; simulation of compound models,
discrete mixtures and compound hierarchical models; credibility theory.
Support for many additional probability distributions to model insurance
loss size and frequency: 23 continuous heavy tailed distributions; the
Poisson-inverse Gaussian discrete distribution; zero-truncated and
zero-modified extensions of the standard discrete distributions. Support
for phase-type distributions commonly used to compute ruin probabilities.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.0.Rd
%doc %{rlibdir}/%{packname}/NEWS.1.Rd
%doc %{rlibdir}/%{packname}/NEWS.2.Rd
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
