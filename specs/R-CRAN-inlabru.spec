%global packname  inlabru
%global packver   2.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.13
Release:          2%{?dist}
Summary:          Spatial Inference using Integrated Nested Laplace Approximation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-utils 
Requires:         R-Matrix 

%description
Facilitates spatial modeling using integrated nested Laplace approximation
via the INLA package (<http://www.r-inla.org>). Additionally, implements a
log Gaussian Cox process likelihood for modeling univariate and spatial
point processes based on ecological survey data. See Yuan Yuan, Fabian E.
Bachl, Finn Lindgren, David L. Borchers, Janine B. Illian, Stephen T.
Buckland, Havard Rue, Tim Gerrodette (2017), <arXiv:1604.06013>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
