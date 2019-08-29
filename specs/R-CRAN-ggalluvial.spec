%global packname  ggalluvial
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Alluvial Diagrams in 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-stats 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Alluvial diagrams use x-splines, sometimes augmented with stacked
histograms, to visualize multi-dimensional or repeated-measures data with
categorical or ordinal variables. They can be viewed as simplified and
standardized Sankey diagrams; see Riehmann, Hanfler, and Froehlich (2005)
<doi:10.1109/INFVIS.2005.1532152> and Rosvall and Bergstrom (2010)
<doi:10.1371/journal.pone.0008694>. This package provides ggplot2 layers
to produce alluvial diagrams from tidy data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
