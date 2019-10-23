%global packname  MTGS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Genomic Selection using Multiple Traits

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MRCE 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MRCE 

%description
Genomic selection (GS) is recent development in animal and plant breeding.
In GS whole genome markers information is used to predict genetic merit of
an individual. This package is basically developed for genomic predictions
by estimating marker effects. These marker effects are then further used
for calculation of genotypic merit of individual i.e. genome estimated
breeding values (GEBVs). However, as genetic correlations between
quantitative traits under breeding studies are obvious. These correlations
indicate that one trait carry information over other traits. Current,
single-trait genomic selection (STGS) methods could not able to utilize
this information. Genomic selection based on multiple traits (MTGS) could
be a better alternative to STGS. This package performs genomic selection
using multi traits information hence named as MTGS i.e. multi trait
genomic selection. MTGS is a comprehensive package which gives single step
solution for genomic selection using various MTGS based methods.

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
