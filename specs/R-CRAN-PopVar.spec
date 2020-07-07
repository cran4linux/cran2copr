%global packname  PopVar
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Genomic Breeding Tools: Genetic Variance Prediction andCross-Validation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-rrBLUP 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-rrBLUP 
Requires:         R-stats 
Requires:         R-utils 

%description
The main attribute of 'PopVar' is the prediction of genetic variance in
bi-parental populations, from which the package derives its name. 'PopVar'
contains a set of functions that use phenotypic and genotypic data from a
set of candidate parents to 1) predict the mean, genetic variance, and
superior progeny value of all, or a defined set of pairwise bi-parental
crosses, and 2) perform cross-validation to estimate genome-wide
prediction accuracy of multiple statistical models. More details are
available in Mohammadi, Tiede, and Smith (2015). Crop Sci.
doi:10.2135/cropsci2015.01.0030. A dataset 'think_barley.rda' is included
for reference and examples.

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
