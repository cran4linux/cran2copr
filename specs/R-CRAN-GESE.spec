%global debug_package %{nil}
%global packname  GESE
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Gene-Based Segregation Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kinship2 
Requires:         R-CRAN-kinship2 

%description
Implements the gene-based segregation test(GESE) and the weighted GESE
test for identifying genes with causal variants of large effects for
family-based sequencing data. The methods are described in Qiao, D. Lange,
C., Laird, N.M., Won, S., Hersh, C.P., et al. (2017).
<DOI:10.1002/gepi.22037>. Gene-based segregation method for identifying
rare variants for family-based sequencing studies. Genet Epidemiol
41(4):309-319. More details can be found at
<http://scholar.harvard.edu/dqiao/gese>.

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
