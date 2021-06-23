%global __brp_check_rpaths %{nil}
%global packname  Yamm
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multivariate Methods Based on Projections and Related Concepts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-depth 
BuildRequires:    R-CRAN-OjaNP 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-depth 
Requires:         R-CRAN-OjaNP 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-interp 

%description
Functionality to compute the projection median via several algorithms.
This package also provides functions to plot different multivariate
medians and multivariate quantiles in two-dimensional and
three-dimensional data respectively. See Chen, F. and Nason, G.P. (2020)
"A new method for computing the projection median, its influence curve and
techniques for the production of projected quantile plots." PLOS One
(accepted for publication).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
