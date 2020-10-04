%global packname  irtoys
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Functions Related to Item Response Theory (IRT)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-ltm 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-ltm 

%description
A collection of functions useful in learning and practicing IRT, which can
be combined into larger programs. Provides basic CTT analysis, a simple
common interface to the estimation of item parameters in IRT models for
binary responses with three different programs (ICL, BILOG-MG, and ltm),
ability estimation (MLE, BME, EAP, WLE, plausible values), item and person
fit statistics, scaling methods (MM, MS, Stocking-Lord, and the complete
Hebaera method), and a rich array of parametric and non-parametric
(kernel) plots. Estimates and plots Haberman's interaction model when all
items are dichotomously scored.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
