%global packname  compareDF
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Do a Git Style Diff of the Rows Between Two Dataframes withSimilar Structure

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-htmlTable >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-tidyr >= 0.4.1
Requires:         R-CRAN-openxlsx >= 4.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-htmlTable >= 1.5
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-tidyr >= 0.4.1

%description
Compares two dataframes which have the same column structure to show the
rows that have changed. Also gives a git style diff format to quickly see
what has changed in addition to summary statistics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
