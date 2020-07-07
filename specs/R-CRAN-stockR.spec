%global packname  stockR
%global packver   1.0.74
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.74
Release:          3%{?dist}
Summary:          Identifying Stocks in Genetic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 

%description
Provides a mixture model for clustering individuals (or sampling groups)
into stocks based on their genetic profile. Here, sampling groups are
individuals that are sure to come from the same stock (e.g. breeding
adults or larvae). The mixture (log-)likelihood is maximised using the
EM-algorithm after find good starting values via a K-means clustering of
the genetic data. Details can be found in Foster, Feutry, Grewe, Berry,
Hui, Davies (2019) Reliably Discriminating Stock Structure with Genetic
Markers: Mixture Models with Robust and Fast Computation. Molecular
Ecology Resources.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
