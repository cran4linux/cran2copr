%global packname  bsts
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          2%{?dist}
Summary:          Bayesian Structural Time Series

License:          LGPL-2.1 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-BoomSpikeSlab >= 1.2.3
BuildRequires:    R-CRAN-Boom >= 0.9.6
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-BoomSpikeSlab >= 1.2.3
Requires:         R-CRAN-Boom >= 0.9.6
Requires:         R-CRAN-xts 

%description
Time series regression using dynamic linear models fit using MCMC. See
Scott and Varian (2014) <DOI:10.1504/IJMMNO.2014.059942>, among many other
sources.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
