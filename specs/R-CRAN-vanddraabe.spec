%global packname  vanddraabe
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Identification and Statistical Analysis of Conserved Waters NearProteins

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-bio3d >= 2.3.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-fastcluster >= 1.1.25
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 0.9.4
Requires:         R-CRAN-openxlsx >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-bio3d >= 2.3.4
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-fastcluster >= 1.1.25
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-cowplot >= 0.9.4

%description
Identify and analyze conserved waters within crystallographic protein
structures and molecular dynamics simulation trajectories. Statistical
parameters for each water cluster, informative graphs, and a PyMOL session
file to visually explore the conserved waters and protein are returned.
Hydrophilicity is the propensity of waters to congregate near specific
protein atoms and is related to conserved waters. An informatics derived
set of hydrophilicity values are provided based on a large, high-quality
X-ray protein structure dataset.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
