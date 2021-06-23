%global __brp_check_rpaths %{nil}
%global packname  spathial
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Evolutionary Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-class 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-irlba 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixStats 
Requires:         R-MASS 
Requires:         R-CRAN-Rtsne 
Requires:         R-class 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-irlba 

%description
A generic tool for manifold analysis. It allows to infer a relevant
transition or evolutionary path which can highlights the features involved
in a specific process. 'spathial' can be useful in all the scenarios where
the temporal (or pseudo-temporal) evolution is the main problem (e.g.
tumor progression). The algorithm for finding the principal path is
described in: Ferrarotti et al., (2019) <doi:10.1109/TNNLS.2018.2884792>."

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/extras
%{rlibdir}/%{packname}/INDEX
