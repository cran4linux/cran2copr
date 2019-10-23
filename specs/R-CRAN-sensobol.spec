%global packname  sensobol
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Computation of High-Order Sobol' Sensitivity Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-boot >= 1.3.20
BuildRequires:    R-CRAN-randtoolbox >= 1.17.1
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-boot >= 1.3.20
Requires:         R-CRAN-randtoolbox >= 1.17.1
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-stats 
Requires:         R-utils 

%description
It allows to rapidly compute, bootstrap and plot up to third-order Sobol'
indices using the estimators by Saltelli et al. 2010
<doi:10.1016/j.cpc.2009.09.018> and Jansen 1999
<doi:10.1016/S0010-4655(98)00154-4>. The 'sensobol' package also
implements the algorithm by Khorashadi Zadeh et al. 2017
<doi:10.1016/j.envsoft.2017.02.001> to calculate the approximation error
in the computation of Sobol' first and total indices, an approach that
allows to robustly screen influential from non-influential model inputs.
Finally, it also provides functions to obtain publication-ready figures of
the model output uncertainty and sensitivity-related analysis.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
