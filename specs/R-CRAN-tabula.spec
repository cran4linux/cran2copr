%global packname  tabula
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}
Summary:          Analysis, Seriation and Visualization of Archaeological CountData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-ca >= 0.71
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-arkhe 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-ca >= 0.71
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-arkhe 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
An easy way to examine archaeological count data. This package provides a
convenient and reproducible toolkit for relative and absolute dating and
analysis of (chronological) patterns. It includes functions for matrix
seriation (reciprocal ranking, CA-based seriation), chronological modeling
and dating of archaeological assemblages and/or objects. Beyond these, the
package provides several tests and measures of diversity: heterogeneity
and evenness (Brillouin, Shannon, Simpson, etc.), richness and rarefaction
(Chao1, Chao2, ACE, ICE, etc.), turnover and similarity
(Brainerd-Robinson, etc.). The package make it easy to visualize count
data and statistical thresholds: rank vs. abundance plots, heatmaps, Ford
(1962) and Bertin (1977) diagrams.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
