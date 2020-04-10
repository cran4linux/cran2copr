%global packname  metaviz
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Forest Plots, Funnel Plots, and Visual Funnel Plot Inference forMeta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.2
BuildRequires:    R-CRAN-metafor >= 1.9.9
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-nullabor >= 0.3.5
BuildRequires:    R-CRAN-ggpubr >= 0.1.6
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-gridExtra >= 2.2
Requires:         R-CRAN-metafor >= 1.9.9
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-nullabor >= 0.3.5
Requires:         R-CRAN-ggpubr >= 0.1.6

%description
A compilation of functions to create visually appealing and
information-rich plots of meta-analytic data using 'ggplot2'. Currently
allows to create forest plots, funnel plots, and many of their variants,
such as rainforest plots, thick forest plots, additional evidence contour
funnel plots, and sunset funnel plots. In addition, functionalities for
visual inference with the funnel plot in the context of meta-analysis are
provided.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
