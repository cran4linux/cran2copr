%global packname  groupdata2
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Creating Groups from Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-numbers >= 0.7.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-numbers >= 0.7.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-utils 

%description
Methods for dividing data into groups. Create balanced partitions and
cross-validation folds. Perform time series windowing and general grouping
and splitting of data. Balance existing groups with up- and downsampling.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
