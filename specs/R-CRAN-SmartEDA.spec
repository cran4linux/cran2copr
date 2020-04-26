%global packname  SmartEDA
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Summarize and Explore the Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sampling >= 2.8
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rmarkdown >= 1.9
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-ISLR >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-sampling >= 2.8
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rmarkdown >= 1.9
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-ISLR >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-scales >= 0.5.0

%description
Exploratory analysis on any input data describing the structure and the
relationships present in the data. The package automatically select the
variable and does related descriptive statistics. Analyzing information
value, weight of evidence, custom tables, summary statistics, graphical
techniques will be performed for both numeric and categorical predictors.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rmd_template
%{rlibdir}/%{packname}/INDEX
