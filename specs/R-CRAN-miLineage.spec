%global __brp_check_rpaths %{nil}
%global packname  miLineage
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Association Tests for Microbial Lineages on a Taxonomic Tree

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geepack 
Requires:         R-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geepack 

%description
A variety of association tests for microbiome data analysis including
Quasi-Conditional Association Tests (QCAT) described in Tang Z.-Z. et
al.(2017) <doi:10.1093/bioinformatics/btw804> and Zero-Inflated
Generalized Dirichlet Multinomial (ZIGDM) tests described in Tang Z.-Z. &
Chen G. (2017, submitted).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
