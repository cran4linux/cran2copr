%global packname  stratamatch
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Stratification and Matching for Large Observational Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.2.0
BuildRequires:    R-survival >= 2.44.1.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-Hmisc >= 4.2.0
Requires:         R-survival >= 2.44.1.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.0

%description
A pilot matching design to automatically stratify and match large
datasets.  The manual_stratify() function allows users to manually
stratify a dataset based on categorical variables of interest, while the
auto_stratify() function does automatically by allocating a held-aside
(pilot) data set, fitting a prognostic score (see Hansen (2008)
<doi:10.1093/biomet/asn004>) on the pilot set, and stratifying the data
set based on prognostic score quantiles.  The strata_match() function then
does optimal matching of the data set in parallel within strata.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
