%global packname  helda
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Preprocess Data and Get Better Insights from Machine LearningModels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-sqldf >= 0.4.11
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-sqldf >= 0.4.11

%description
The main focus is on preprocessing and data visualization of machine
learning models performances. Some functions allow to fill in gaps in time
series using linear interpolation on panel data, some functions permit to
draw lift effect and lift curve in order to benchmark machine learning
models or you can even find the optimal number of clusters in
agglomerative clustering algorithm.

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
