%global packname  compositions
%global packver   1.40-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.40.5
Release:          3%{?dist}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-bayesm 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-bayesm 

%description
Provides functions for the consistent analysis of compositional data (e.g.
portions of substances) and positive numbers (e.g. concentrations) in the
way proposed by J. Aitchison and V. Pawlowsky-Glahn.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
