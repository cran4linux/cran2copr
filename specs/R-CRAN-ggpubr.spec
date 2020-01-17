%global packname  ggpubr
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          'ggplot2' Based Publication Ready Plots

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-ggsci 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-rlang 

%description
The 'ggplot2' package is excellent and flexible for elegant data
visualization in R. However the default generated plots requires some
formatting before we can send them for publication. Furthermore, to
customize a 'ggplot', the syntax is opaque and this raises the level of
difficulty for researchers with no advanced R programming skills. 'ggpubr'
provides some easy-to-use functions for creating and customizing
'ggplot2'- based publication ready plots.

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
%{rlibdir}/%{packname}/demo-data
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
