%global packname  biclustermd
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Biclustering with Missing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-biclust >= 2.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-nycflights13 >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-phyclust >= 0.1.24
BuildRequires:    R-CRAN-clusteval >= 0.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-biclust >= 2.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-nycflights13 >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-phyclust >= 0.1.24
Requires:         R-CRAN-clusteval >= 0.1

%description
Biclustering is a statistical learning technique that simultaneously
partitions and clusters rows and columns of a data matrix. Since the
solution space of biclustering is in infeasible to completely search with
current computational mechanisms, this package uses a greedy heuristic.
The algorithm featured in this package is, to the best our knowledge, the
first biclustering algorithm to work on data with missing values. Li, J.,
Reisner, J., Pham, H., Olafsson, S., and Vardeman, S. (2020) Biclustering
with Missing Data. Information Sciences, 510, 304–316.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
