%global __brp_check_rpaths %{nil}
%global packname  seedCCA
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Seeded Canonical Correlation Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CCA 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-CCA 
Requires:         R-CRAN-corpcor 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions for dimension reduction through the seeded canonical correlation
analysis are provided. A classical canonical correlation analysis (CCA) is
one of useful statistical methods in multivariate data analysis, but it is
limited in use due to the matrix inversion for large p small n data. To
overcome this, a seeded CCA has been proposed in Im, Gang and Yoo (2015)
<DOI:10.1002/cem.2691>. The seeded CCA is a two-step procedure. The sets
of variables are initially reduced by successively projecting cov(X,Y) or
cov(Y,X) onto cov(X) and cov(Y), respectively, without loss of information
on canonical correlation analysis, following Cook, Li and Chiaromonte
(2007) <DOI:10.1093/biomet/asm038> and Lee and Yoo (2014)
<DOI:10.1111/anzs.12057>. Then, the canonical correlation is finalized
with the initially-reduced two sets of variables.

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
%{rlibdir}/%{packname}/INDEX
