%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggdist
%global packver   3.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizations of Distributions and Uncertainty

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-distributional >= 0.3.2
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-distributional >= 0.3.2
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rcpp 

%description
Provides primitives for visualizing distributions using 'ggplot2' that are
particularly tuned for visualizing uncertainty in either a frequentist or
Bayesian mode. Both analytical distributions (such as frequentist
confidence distributions or Bayesian priors) and distributions represented
as samples (such as bootstrap distributions or Bayesian posterior samples)
are easily visualized. Visualization primitives include but are not
limited to: points with multiple uncertainty intervals, eye plots
(Spiegelhalter D., 1999)
<https://ideas.repec.org/a/bla/jorssa/v162y1999i1p45-58.html>, density
plots, gradient plots, dot plots (Wilkinson L., 1999)
<doi:10.1080/00031305.1999.10474474>, quantile dot plots (Kay M., Kola T.,
Hullman J., Munson S., 2016) <doi:10.1145/2858036.2858558>, complementary
cumulative distribution function barplots (Fernandes M., Walls L., Munson
S., Hullman J., Kay M., 2018) <doi:10.1145/3173574.3173718>, and fit
curves with multiple uncertainty ribbons.

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
