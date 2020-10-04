%global packname  sdglinkage
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Synthetic Data Generation for Linkage Methods Development

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn >= 4.4
BuildRequires:    R-CRAN-arsenal >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-visNetwork >= 2.0.6
BuildRequires:    R-CRAN-synthpop >= 1.5.1
BuildRequires:    R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-bnlearn >= 4.4
Requires:         R-CRAN-arsenal >= 3.3.0
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-visNetwork >= 2.0.6
Requires:         R-CRAN-synthpop >= 1.5.1
Requires:         R-CRAN-reshape >= 0.8.8

%description
A tool for synthetic data generation that can be used for linkage method
development, with elements of i) gold standard file with complete and
accurate information and ii) linkage files that are corrupted as we often
see in raw dataset.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
