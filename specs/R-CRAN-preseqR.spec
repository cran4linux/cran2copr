%global packname  preseqR
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Predicting Species Accumulation Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-polynom 
Requires:         R-graphics 
Requires:         R-stats 

%description
Originally as an R version of Preseq <doi:10.1038/nmeth.2375>, the package
has extended its functionality to predict the r-species accumulation curve
(r-SAC), which is the number of species represented at least r times as a
function of the sampling effort. When r = 1, the curve is known as the
species accumulation curve, or the library complexity curve in
high-throughput genomic sequencing. The package includes both parametric
and nonparametric methods, as described by Deng C, et al. (2018)
<arXiv:1607.02804v3>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
