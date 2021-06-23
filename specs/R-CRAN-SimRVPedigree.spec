%global __brp_check_rpaths %{nil}
%global packname  SimRVPedigree
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          Simulate Pedigrees Ascertained for a Rare Disease

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-methods >= 3.4.0
BuildRequires:    R-CRAN-kinship2 >= 1.6.4
BuildRequires:    R-CRAN-dplyr >= 0.7.4
Requires:         R-stats >= 3.4.0
Requires:         R-methods >= 3.4.0
Requires:         R-CRAN-kinship2 >= 1.6.4
Requires:         R-CRAN-dplyr >= 0.7.4

%description
Routines to simulate and manipulate pedigrees ascertained to contain
multiple family members affected by a rare disease. Christina Nieuwoudt,
Samantha J Jones, Angela Brooks-Wilson, and Jinko Graham (2018)
<doi:10.1101/234153>.

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
