%global packname  sklarsomega
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Measuring Agreement Using Sklar's Omega Coefficient

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-spam 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-Matrix 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-spam 

%description
Provides tools for applying Sklar's Omega (Hughes, 2018)
<arXiv:1803.02734> methodology to nominal, ordinal, interval, or ratio
scores. The framework can accommodate any number of units, any number of
coders, and missingness; and can be used to measure agreement with a gold
standard, intra-coder agreement, and/or inter-coder agreement. Frequentist
inference is supported for all levels of measurement. Bayesian inference
is supported for interval and ratio scores.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
