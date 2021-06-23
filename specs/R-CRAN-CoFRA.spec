%global __brp_check_rpaths %{nil}
%global packname  CoFRA
%global packver   0.1002
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1002
Release:          3%{?dist}%{?buildtag}
Summary:          Complete Functional Regulation Analysis

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-gplots 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
Calculates complete functional regulation analysis and visualize the
results in a single heatmap. The provided example data is for biological
data but the methodology can be used for large data sets to compare
quantitative entities that can be grouped. For example, a store might
divide entities into cloth, food, car products etc and want to see how
sales changes in the groups after some event. The theoretical background
for the calculations are provided in New insights into functional
regulation in MS-based drug profiling, Ana Sofia Carvalho, Henrik Molina &
Rune Matthiesen, Scientific Reports <doi:10.1038/srep18826>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
