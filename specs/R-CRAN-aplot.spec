%global packname  aplot
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Decorate a 'ggplot' with Associated Information

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 

%description
For many times, we are not just aligning plots as what 'cowplot' and
'patchwork' did. Users would like to align associated information that
requires axes to be exactly matched in subplots, e.g. hierarchical
clustering with a heatmap. This package provides utilities to aligns
associated subplots to a main plot at different sides (left, right, top
and bottom) with axes exactly matched.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
