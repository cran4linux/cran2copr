%global packname  clhs
%global packver   0.7-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          3%{?dist}
Summary:          Conditioned Latin Hypercube Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-cluster 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-scales 
Requires:         R-cluster 

%description
Conditioned Latin hypercube sampling, as published by Minasny and
McBratney (2006) <DOI:10.1016/j.cageo.2005.12.009>. This method proposes
to stratify sampling in presence of ancillary data. An extension of this
method, which propose to associate a cost to each individual and take it
into account during the optimisation process, is also proposed (Roudier et
al., 2012, <DOI:10.1201/b12728>).

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
