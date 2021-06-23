%global __brp_check_rpaths %{nil}
%global packname  MPTinR
%global packver   1.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Multinomial Processing Tree Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a user-friendly way for the analysis of multinomial processing
tree (MPT) models (e.g., Riefer, D. M., and Batchelder, W. H. [1988].
Multinomial modeling and the measurement of cognitive processes.
Psychological Review, 95, 318-339) for single and multiple datasets. The
main functions perform model fitting and model selection. Model selection
can be done using AIC, BIC, or the Fisher Information Approximation (FIA)
a measure based on the Minimum Description Length (MDL) framework. The
model and restrictions can be specified in external files or within an R
script in an intuitive syntax or using the context-free language for MPTs.
The 'classical' .EQN file format for model files is also supported.
Besides MPTs, this package can fit a wide variety of other cognitive
models such as SDT models (see fit.model). It also supports multicore
fitting and FIA calculation (using the snowfall package), can generate or
bootstrap data for simulations, and plot predicted versus observed data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
