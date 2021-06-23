%global __brp_check_rpaths %{nil}
%global packname  ModStatR
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Modelling in Action with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-jmuOutlier 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-gsl 
Requires:         R-stats 
Requires:         R-CRAN-boot 
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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
