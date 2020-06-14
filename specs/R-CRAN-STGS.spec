%global packname  STGS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Genomic Selection using Single Trait

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-brnn 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rrBLUP 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-brnn 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rrBLUP 

%description
Genomic Selection (GS) is a latest development in animal and plant
breeding where whole genome markers information is used to predict genetic
merit of an individuals in a practical breeding programme. GS is one of
the promising tool for improving genetic gain in animal and plants in
today’s scenario. This package is basically developed for genomic
predictions by estimating marker effects. These marker effects further
used for calculation of genotypic merit of individual i.e. genome
estimated breeding values (GEBVs). Genomic selection may be based on
single trait or multi traits information. This package performs genomic
selection only for single traits hence named as STGS i.e. single trait
genomic selection. STGS is a comprehensive package which gives single step
solution for genomic selection based on most commonly used statistical
methods.

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
