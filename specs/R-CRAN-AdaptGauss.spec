%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AdaptGauss
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Mixture Models (GMM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DataVisualizations 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-pracma 
Requires:         R-methods 
Requires:         R-CRAN-DataVisualizations 
Requires:         R-CRAN-plotly 

%description
Multimodal distributions can be modelled as a mixture of components. The
model is derived using the Pareto Density Estimation (PDE) for an
estimation of the pdf. PDE has been designed in particular to identify
groups/classes in a dataset. Precise limits for the classes can be
calculated using the theorem of Bayes. Verification of the model is
possible by QQ plot, Chi-squared test and Kolmogorov-Smirnov test. The
package is based on the publication of Ultsch, A., Thrun, M.C.,
Hansen-Goos, O., Lotsch, J. (2015) <DOI:10.3390/ijms161025897>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
