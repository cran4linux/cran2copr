%global packname  CAinterprTools
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Graphical Aid in Correspondence Analysis Interpretation andSignificance Testings

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-graphics >= 3.4.3
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-utils >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-cluster >= 2.0.7
BuildRequires:    R-CRAN-FactoMineR >= 1.40
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-RcmdrMisc >= 1.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.0
BuildRequires:    R-CRAN-ca >= 0.70
BuildRequires:    R-CRAN-classInt >= 0.2.3
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-graphics >= 3.4.3
Requires:         R-stats >= 3.4.3
Requires:         R-utils >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-cluster >= 2.0.7
Requires:         R-CRAN-FactoMineR >= 1.40
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-RcmdrMisc >= 1.0
Requires:         R-CRAN-ggrepel >= 0.8.0
Requires:         R-CRAN-ca >= 0.70
Requires:         R-CRAN-classInt >= 0.2.3

%description
Allows to plot a number of information related to the interpretation of
Correspondence Analysis' results. It provides the facility to plot the
contribution of rows and columns categories to the principal dimensions,
the quality of points display on selected dimensions, the correlation of
row and column categories to selected dimensions, etc. It also allows to
assess which dimension(s) is important for the data structure
interpretation by means of different statistics and tests. The package
also offers the facility to plot the permuted distribution of the table
total inertia as well as of the inertia accounted for by pairs of selected
dimensions. Different facilities are also provided that aim to produce
interpretation-oriented scatterplots. Reference: Alberti 2015
<doi:10.1016/j.softx.2015.07.001>.

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
%{rlibdir}/%{packname}/INDEX
