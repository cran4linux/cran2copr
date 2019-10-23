%global packname  randomForestExplainer
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}
Summary:          Explaining and Visualizing Random Forests in Terms of VariableImportance

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.12
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rmarkdown >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-GGally >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-ranger >= 0.9.0
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-ggrepel >= 0.6.5
BuildRequires:    R-CRAN-DT >= 0.2
Requires:         R-CRAN-randomForest >= 4.6.12
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rmarkdown >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-GGally >= 1.3.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-ranger >= 0.9.0
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-ggrepel >= 0.6.5
Requires:         R-CRAN-DT >= 0.2

%description
A set of tools to help explain which variables are most important in a
random forests. Various variable importance measures are calculated and
visualized in different settings in order to get an idea on how their
importance changes depending on our criteria (Hemant Ishwaran and Udaya B.
Kogalur and Eiran Z. Gorodeski and Andy J. Minn and Michael S. Lauer
(2010) <doi:10.1198/jasa.2009.tm08622>, Leo Breiman (2001)
<doi:10.1023/A:1010933404324>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
