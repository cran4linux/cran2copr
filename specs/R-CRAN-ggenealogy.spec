%global __brp_check_rpaths %{nil}
%global packname  ggenealogy
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Visualization Tools for Genealogical Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-CRAN-reshape2 >= 1.4
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-igraph >= 0.7.1
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-igraph >= 0.7.1

%description
Methods for searching through genealogical data and displaying the
results. Plotting algorithms assist with data exploration and
publication-quality image generation. Includes interactive genealogy
visualization tools. Provides parsing and calculation methods for
variables in descendant branches of interest. Uses the Grammar of
Graphics.

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
%{rlibdir}/%{packname}
