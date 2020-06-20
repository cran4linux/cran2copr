%global packname  likert
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Analysis and Visualization Likert Items

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-plyr 

%description
An approach to analyzing Likert response items, with an emphasis on
visualizations. The stacked bar plot is the preferred method for
presenting Likert results. Tabular results are also implemented along with
density plots to assist researchers in determining whether Likert
responses can be used quantitatively instead of qualitatively. See the
likert(), summary.likert(), and plot.likert() functions to get started.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
