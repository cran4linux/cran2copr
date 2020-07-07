%global packname  FunCC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Functional Cheng and Church Bi-Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.1
Requires:         R-core >= 3.5.1
BuildArch:        noarch
BuildRequires:    R-CRAN-narray 
BuildRequires:    R-CRAN-biclust 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-narray 
Requires:         R-CRAN-biclust 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 

%description
The FunCC algorithm allows to apply the FunCC algorithm to simultaneously
cluster the rows and the columns of a data matrix whose inputs are
functions.

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
