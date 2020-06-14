%global packname  rbtt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Alternative Bootstrap-Based t-Test Aiming to Reduce Type-I Errorfor Non-Negative, Zero-Inflated Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 

%description
Tu & Zhou (1999)
<doi:10.1002/(SICI)1097-0258(19991030)18:20%3C2749::AID-SIM195%3E3.0.CO;2-C>
showed that comparing the means of populations whose data-generating
distributions are non-negative with excess zero observations is a problem
of great importance in the analysis of medical cost data. In the same
study, Tu & Zhou discuss that it can be difficult to control type-I error
rates of general-purpose statistical tests for comparing the means of
these particular data sets. This package allows users to perform a
modified bootstrap-based t-test that aims to better control type-I error
rates in these situations.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
