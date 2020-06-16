%global packname  SimRVSequences
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Simulate Genetic Sequence Data for Pedigrees

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-CRAN-kinship2 >= 1.6.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-Matrix >= 1.2.12
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-intervals >= 0.15.1
BuildRequires:    R-CRAN-SimRVPedigree >= 0.1.0
Requires:         R-methods >= 3.5.0
Requires:         R-stats >= 3.3.0
Requires:         R-CRAN-kinship2 >= 1.6.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-Matrix >= 1.2.12
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-intervals >= 0.15.1
Requires:         R-CRAN-SimRVPedigree >= 0.1.0

%description
Methods to simulate genetic sequence data for pedigrees, with
functionality to simulate genetic heterogeneity among pedigrees. Christina
Nieuwoudt, Angela Brooks-Wilson, and Jinko Graham (2019)
<doi:10.1101/534552>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
