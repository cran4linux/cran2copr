%global packname  r.jive
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Perform JIVE Decomposition for Multi-Source Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SpatioTemporal 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-SpatioTemporal 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-stats 

%description
Performs the JIVE decomposition on a list of data sets when the data share
a dimension, returning low-rank matrices that capture the joint and
individual structure of the data [O'Connell, MJ and Lock, EF (2016)
<doi:10.1093/bioinformatics/btw324>]. It provides two methods of rank
selection when the rank is unknown, a permutation test and a BIC selection
algorithm. Also included in the package are three plotting functions for
visualizing the variance attributed to each data source: a bar plot that
shows the percentages of the variability attributable to joint and
individual structure, a heatmap that shows the structure of the
variability, and principal component plots.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
