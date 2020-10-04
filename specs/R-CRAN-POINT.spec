%global packname  POINT
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Protein Structure Guided Local Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rARPACK 
Requires:         R-Matrix 
Requires:         R-CRAN-CompQuadForm 

%description
Provides an implementation of a rare variant association test that
utilizes protein tertiary structure to increase signal and to identify
likely causal variants. Performs structure-guided collapsing, which leads
to local tests that borrow information from neighboring variants on a
protein and that provide association information on a variant-specific
level. For details of the implemented method see West, R. M., Lu, W.,
Rotroff, D. M., Kuenemann, M., Chang, S-M., Wagner M. J., Buse, J. B.,
Motsinger-Reif, A., Fourches, D., and Tzeng, J-Y. (2019)
<doi:10.1371/journal.pcbi.1006722>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
