%global packname  cati
%global packver   0.99.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.3
Release:          3%{?dist}
Summary:          Community Assembly by Traits: Individuals and Beyond

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-hypervolume 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-vegan 
Requires:         R-nlme 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-hypervolume 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-vegan 

%description
Detect and quantify community assembly processes using trait values of
individuals or populations, the T-statistics (Violle et al. (2012)
<doi:10.1016/j.tree.2011.11.014>) and other metrics, and dedicated null
models described in Taudiere & Violle (2016) <doi:10.1111/ecog.01433>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
