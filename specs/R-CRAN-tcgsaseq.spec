%global packname  tcgsaseq
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          3%{?dist}
Summary:          Time-Course Gene Set Analysis for RNA-Seq Data

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-GSA 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-utils 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-GSA 
Requires:         R-KernSmooth 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-utils 

%description
Analyze RNA-seq data with variance component score test accounting for
data heteroscedasticity through precision weights. Perform both gene-wise
and gene set analyses, and can deal with longitudinal data. Method is
detailed in: Agniel D & Hejblum BP (2017) Variance component score test
for time-course gene set analysis of longitudinal RNA-seq data,
Biostatistics, 18(4):589-604.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
