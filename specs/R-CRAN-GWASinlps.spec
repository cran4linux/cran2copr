%global __brp_check_rpaths %{nil}
%global packname  GWASinlps
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Nonlocal Prior Based Iterative SNP Selection Tool forGenome-Wide Association Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mombf 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-horseshoe 
Requires:         R-CRAN-mombf 
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-horseshoe 

%description
Performs variable selection with data from Genome-wide association studies
(GWAS) combining, in an iterative variable selection framework, the
computational efficiency of the screen-and-select approach based on some
association learning and the parsimonious uncertainty quantification
provided by the use of nonlocal priors, as described in Sanyal et al.
(2018).

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
