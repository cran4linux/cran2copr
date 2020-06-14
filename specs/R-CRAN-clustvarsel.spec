%global packname  clustvarsel
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          2%{?dist}
Summary:          Variable Selection for Gaussian Model-Based Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 5.3
BuildRequires:    R-CRAN-BMA >= 3.18
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-mclust >= 5.3
Requires:         R-CRAN-BMA >= 3.18
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
Variable selection for Gaussian model-based clustering as implemented in
the 'mclust' package. The methodology allows to find the (locally) optimal
subset of variables in a data set that have group/cluster information. A
greedy or headlong search can be used, either in a forward-backward or
backward-forward direction, with or without sub-sampling at the
hierarchical clustering stage for starting 'mclust' models. By default the
algorithm uses a sequential search, but parallelisation is also available.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
