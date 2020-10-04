%global packname  ModStatR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Modelling in Action with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-BioStatR 
BuildRequires:    R-CRAN-jmuOutlier 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-gsl 
Requires:         R-stats 
Requires:         R-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-BioStatR 
Requires:         R-CRAN-jmuOutlier 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-gsl 

%description
Datasets and functions for the book "Modélisation statistique par la
pratique avec R", F. Bertrand, E. Claeys and M. Maumy-Bertrand (2019,
ISBN:9782100793525, Dunod, Paris). The first chapter of the book is
dedicated to an introduction to the R statistical software. The second
chapter deals with correlation analysis: Pearson, Spearman and Kendall
simple, multiple and partial correlation coefficients. New wrapper
functions for permutation tests or bootstrap of matrices of correlation
are provided with the package. The third chapter is dedicated to data
exploration with factorial analyses (PCA, CA, MCA, MDA) and clustering.
The fourth chapter is dedicated to regression analysis: fitting and model
diagnostics are detailed. The exercises focus on covariance analysis,
logistic regression, Poisson regression, two-way analysis of variance for
fixed or random factors. Various example datasets are shipped with the
package: for instance on pokemon, world of warcraft, house tasks or food
nutrition analyses.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
